mkdir data
cd data
wget http://www.schonlau.net/masquerade/MasqueradeDat.gz
mkdir masquerade_users
gzip -d MasqueradeDat.gz
tar -xf MasqueradeDat -C masquerade_users
rm MasqueradeDat

wget http://www.schonlau.net/masquerade/masquerade_summary.txt
