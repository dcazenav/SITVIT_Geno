from django.db import models

# Create your models here.
class Souchefile(models.Model):
    RunName = models.CharField("RunName", max_length=255)
    SpoligoType_MiruHero = models.CharField("SpoligoType(MiruHero)", max_length=30)
    SpoligoType_Spotyping = models.CharField("SpoligoType(Spotyping)", max_length=30)
    MiruType_MiruHero = models.CharField("MiruType(MiruHero)", max_length=30)
    MiruType_mirureader = models.CharField("MiruType(mirureader)", max_length=30)
    Lineage_MiruHero = models.CharField("Lineage(MiruHero)", max_length=30)
    Lineages_tbprofiler = models.CharField("Lineages(tb-profiler)", max_length=75)
    Resistance_tbprofiler = models.CharField("Resistance(tb-profiler)", max_length=75)
    Family_SpolLineages = models.CharField("Family(SpolLineages)", max_length=75)
    Country = models.CharField("Country", max_length=75)

# class Souche(models.Model):
#     FilePath = models.CharField(_("FilePath"), max_length=255)
#     RunName = models.CharField(_("RunName"), max_length=255)
#     SpoligoTypeMiruHero = models.CharField(_("SpoligoType(MiruHero)"), max_length=30)
#     SpoligoTypeSpotyping = models.CharField(_("SpoligoType(Spotyping)"), max_length=30)
#     MiruTypeMiruHero = models.CharField(_("MiruType(MiruHero)"), max_length=30)
#     MiruTypemirureader = models.CharField(_("MiruType(mirureader)"), max_length=30)
#     LineageMiruHero = models.CharField(_("Lineage(MiruHero)"), max_length=30)
#     Lineagestbprofiler = models.CharField(_("Lineages(tb-profiler)"), max_length=75)
#     Resistancetbprofiler = models.CharField(_("Resistance(tb-profiler)"), max_length=75)
#     FamilySpolLineages = models.CharField(_("Family(SpolLineages)"), max_length=75)
