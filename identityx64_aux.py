# -*- coding: utf-8 -*-
import arcpy,os,time,exceptions
try:
    t_inicio=time.clock()# captura el tiempo de inicio del proceso
    arcpy.env.overwriteOutput = True

    dic_acentos={"---":" ","***a***":"\xc3\xa1","***e***":"\xc3\xa9",
    "***i***":"\xc3\xad", "***o***":"\xc3\xb3","***u***":"\xc3\xba",
    "***n***": "\xc3\xb1","***A***":"\xc3\x81","***E***":"\xc3\x89",
    "***I***":"\xc3\x8d", "***O***":"\xc3\x93","***Ú***":"\xc3\x9a","***N***":"\xc3\x91"}

    def cambia_caracteres(infea):
        for xx in dic_acentos:# ciclo que reemplaza las letras por los carateres especiales
            infea=infea.replace(xx,dic_acentos[xx])
        return infea


    infea=arcpy.GetParameterAsText(0)
    segunda_capa= arcpy.GetParameterAsText(1)
    join_attributes=arcpy.GetParameterAsText(2)
    gdb_salida=arcpy.GetParameterAsText(3)
    capa_salida=arcpy.GetParameterAsText(4)


    infea = cambia_caracteres(infea)
    segunda_capa = cambia_caracteres(segunda_capa)
    gdb_salida = cambia_caracteres(gdb_salida)
    capa_salida = cambia_caracteres(capa_salida)

    arcpy.env.workspace = gdb_salida



    if __name__ == '__main__':
        print "Ejecutando identity a 64bits ...."
        print infea , segunda_capa,capa_salida,gdb_salida
        arcpy.Identity_analysis(in_features=infea,identity_features=segunda_capa, out_feature_class=gdb_salida+"\\"+capa_salida,join_attributes=join_attributes)

except exceptions.Exception as e:
    print e.__class__, e.__doc__, e.message
    os.system("pause")

