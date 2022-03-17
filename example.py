def read_kddcup1999():
  with open('kddcup.data_10_percent_corrected', 'r') as f:
    top10=f.read(100)
    print(top10)
read_kddcup1999()