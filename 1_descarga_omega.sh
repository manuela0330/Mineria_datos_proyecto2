AR="201.6975"
DEC="-47.2795"

echo "Iniciando con la descarga de datos para Omega Centauri"

ADQL="SELECT source, RA_ICRS, DE_ICRS, pmRA, pmDE, Gmag, BPmag, RPmag FROM \"I/355/gaiadr3\" WHERE 1=CONTAINS(POINT('ICRS', RA_ICRS, DE_ICRS), CIRCLE('ICRS', $AR, $DEC, 0.5))"

URL_ADQL=$(echo $ADQL | sed 's/ /+/g')

ENDPOINT="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

echo "conectando con el servidor VizieR"

curl -L -o  omega_bruto.csv "$ENDPOINT$URL_ADQL"

echo "Descarga completada, el archivo omega_bruto.csv se ha creado exitosamente"
