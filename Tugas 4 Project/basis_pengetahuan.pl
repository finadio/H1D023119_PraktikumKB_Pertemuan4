% GEJALA UTAMA
gejala(1, 'terdapat bercak daun berwarna coklat dengan pusat abu-abu').
gejala(2, 'daun menguning dari ujung kemudian layu').
gejala(3, 'terlihat bercak memanjang berwarna coklat pada daun').
gejala(4, 'ada bintik-bintik kecil berwarna kuning pada daun').
gejala(5, 'daun memiliki lapisan putih seperti tepung').
gejala(6, 'tanaman padi kerdil dan pertumbuhan terhambat').
gejala(7, 'daun menggulung dan berwarna kuning-oranye').
gejala(8, 'malai tidak keluar atau hampa').
gejala(9, 'akar berwarna hitam dan busuk').
gejala(10, 'terdapat bercak daun dengan tepi kuning').

% BASIS PENGETAHUAN PENYAKIT
penyakit('Hawar Daun Bakteri', [1,3,9,10], 
    'SOLUSI SPESIFIK:\n'
    '1. Gunakan varietas tahan (Inpari 30)\n'
    '2. Semprot bakterisida Streptomycin 20%\n'
    '3. Kurangi pupuk nitrogen\n'
    '4. Rotasi tanaman dengan palawija').

penyakit('Blas', [2,3,7,8], 
    'SOLUSI SPESIFIK:\n'
    '1. Aplikasikan fungisida Tricyclazole\n'
    '2. Atur jarak tanam 30x30 cm\n'
    '3. Hindari pupuk nitrogen berlebihan\n'
    '4. Keringkan sawah periodik').

penyakit('Tungro', [1,2,5,6], 
    'SOLUSI SPESIFIK:\n'
    '1. Kendalikan wereng hijau (vektor)\n'
    '2. Tanam varietas tahan (Inpari 36)\n'
    '3. Tanam serempak di wilayah luas\n'
    '4. Cabut tanaman terinfeksi').

penyakit('Busuk Batang', [6,8,9], 
    'SOLUSI SPESIFIK:\n'
    '1. Berikan fungisida sistemik\n'
    '2. Perbaiki drainase sawah\n'
    '3. Gunakan pupuk kalium\n'
    '4. Hindari luka mekanis').

% DIAGNOSA PASTI
diagnosa(Gejala, Penyakit, Solusi) :-
    penyakit(Penyakit, GejalaPenyakit, Solusi),
    hitung_kecocokan(Gejala, GejalaPenyakit, Cocok),
    length(GejalaPenyakit, Total),
    Cocok >= max(2, ceiling(Total*0.5)).  % Minimal 2 gejala atau 50% gejala terpenuhi

% DIAGNOSA UMUM JIKA GEJALA SEDIKIT
diagnosa(Gejala, 'Gangguan Pertumbuhan', 
    'SOLUSI UMUM:\n'
    '1. Perbaiki kualitas tanah\n'
    '2. Gunakan pupuk berimbang\n'
    '3. Optimalkan pengairan\n'
    '4. Pantau perkembangan tanaman') :-
    length(Gejala, Jumlah),
    Jumlah < 2.

% HITUNG KECOCOKAN GEJALA
hitung_kecocokan(_, [], 0).
hitung_kecocokan(Gejala, [G|Gs], N) :-
    (member(G, Gejala) -> N1 is 1 ; N1 is 0),
    hitung_kecocokan(Gejala, Gs, N2),
    N is N1 + N2.