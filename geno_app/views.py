import json

import numpy as np
from django.shortcuts import render, redirect
from django.http import HttpResponse

from detect_delimiter import detect
import numpy


from .models import Souchefile


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return render(request, "../templates/geno_app/application/home.html")


def database_description(request):
    return render(request, "../templates/geno_app/application/database_description.html", locals())


def search(request):
    souchefiles = Souchefile.objects.all()
    return render(request, "../templates/geno_app/application/search.html", {'souchefiles': souchefiles})


def analysis(request):
    return render(request, "../templates/geno_app/application/analysis.html", locals())

def refseq(request):
    return render(request, "../templates/geno_app/application/refseq.html", locals())


def online_tools(request):
    return render(request, "../templates/geno_app/application/online_tools.html", locals())

def import_data(request):
    error = False
    info = []
    if 'import' in request.POST:
        csv_file = request.FILES["csv_file"]
        # print(request.FILES["csv_file"])
        if not csv_file.name.endswith(('.csv')):
            error = True
            return render(request, 'geno_app/application/refseq.html', locals())
        else:
            csv_file = request.FILES["csv_file"].read().decode("utf-8").split()
            for elmt in csv_file:
                info.append(elmt.split(detect(elmt)))
            request.session['info'] = info
            return redirect(import_data)

    elif 'import_load' in request.POST:
    #     #print(request.get_all('csv_file'))
    #     #csv_file = request.FILES["csv_file"]
    #     csv_file2 = request.FILES['csv_file2']
    #     print(request.FILES['csv_file2'])
    #     if not csv_file2.name.endswith('.csv'):
    #         error = True
    #         return render(request, 'phylEntropy/import_data.html', locals())
    #     else:

        # print(request.POST)
        csv_file2 = request.FILES["csv_file2"].read().decode("utf-8").split()
        # print(csv_file2)
        for elmt in csv_file2:
            info.append(elmt.split(detect(elmt)))
        request.session['info'] = info
        return redirect(import_data)

    if 'info' in request.session:
        fichier = request.session['info']
        info_submit = True
        print("info_fichie", fichier)
    else:
        info_submit = False
    #context = {'files': files}
    return render(request, 'geno_app/application/refseq.html', locals())

def ajax_1(request):
    if request.method == 'POST':
        data = json.loads(request.POST['tasks'])
        data2 = json.loads(request.POST['labelSeq'])
        index_entete = json.loads(request.POST['entete'])
        request.session['data_file'] = data
        request.session['algo'] = request.POST['algo']
        request.session['labelSeq'] = data2
        request.session['entete'] = index_entete
        return HttpResponse('')


def reduce_table(table,labelSeq):
    taille1=len(table)
    index_ban=[]
    tab_reduce=[]
    label_reduce=[]
    index_sommet={}
    reverse_index={}
    ensemble=[]
    for i in range(len(labelSeq)):
        index_sommet[labelSeq[i]]=i
        reverse_index[i]= [labelSeq[i]]

    for i in range(taille1):
        verif = 0
        taille2= len(table[i])
        for j in range(taille2):
            if table[i][j] ==0:
                if i not in index_ban:
                    index_ban.append(i)

                tab1=reverse_index[index_sommet[labelSeq[i]]]
                tab2=reverse_index[index_sommet[labelSeq[j]]]
                for elmt in tab1 :
                    if elmt not in tab2:
                        tab2.append(elmt)
                reverse_index[index_sommet[labelSeq[j]]]=tab2
                for bct in reverse_index[index_sommet[labelSeq[j]]]:
                    index_sommet[bct]=index_sommet[labelSeq[j]]
                verif=1

        if verif==0:
            tmp = []
            for cpt in range(taille2):
                if cpt not in index_ban:
                   tmp.append(table[i][cpt])
            tab_reduce.append(tmp)
    deja=[]
    for key,value in index_sommet.items():
        if value not in deja:
            ensemble.append(reverse_index[value])
            deja.append(value)

    for i in range(len(ensemble)):
        chn = ""
        for j in range(len(ensemble[i])):
            chn += ensemble[i][j]
            if j < len(ensemble[i]) - 1:
                chn += "+"
        label_reduce.append(chn)

    return tab_reduce,label_reduce,ensemble


def run_algo(request):
    if 'data_file' in request.session and 'algo' in request.session:
        data = request.session['data_file']
        # if not data:
        #     messages.warning(request, 'Select checkboxes')
        # else:
        # nb_bact = len(data[0])
        fichier = request.session['info']
        entete_colonne_selected = []
        index_entete = request.session['entete']
        algo = request.session['algo']
        labelSeq = request.session['labelSeq']
        nb_bact = len(data[0])
        chaine = []
        rows_bact = []
        tab_distance = []
        nb_var = len(data)

        print("fichier", fichier)
        # entete sélectionnersur la première ligne du fichier
        for j in index_entete:
            entete_colonne_selected.append(fichier[0][j])
        # création des chaines sring a partir du caractère de chaque colonnes
        for i in range(nb_bact):
            tmp = ''
            tmp2 = []
            # nombre de variable
            for j in range(len(data)):
                tmp = tmp + data[j][i]
                tmp2.append(data[j][i])
            chaine.append(tmp)
            rows_bact.append(tmp2)
        matrice = (nb_bact, nb_bact)
        matrice = np.zeros(matrice, dtype='int')

        for i in range(len(chaine)):
            for j in range(i + 1, len(chaine)):
                count = sum(1 for a, b in zip(chaine[i], chaine[j]) if a != b)
                matrice[i][j] = count
                matrice[j][i] = count
        for j in range(nb_bact):
            new = []
            for i in range(j):
                if j != 0:
                    new.append(matrice[j][i])
            tab_distance.append(new)
        tab_reduce, label_reduce, ensemble_seq = reduce_table(tab_distance, labelSeq)

