# SPRAWOZDANIE NTPD LAB NR2 
Cel ćwiczenia: Celem tego ćwiczenia jest poznanie narzędzia MLflow

# ZADANIE 1 
## Przygotowanie środowiska i instalacja MLflow 
<img width="634" height="23" alt="image" src="https://github.com/user-attachments/assets/668b76ce-3628-4414-8be4-3d8c162404ec" />
Do środowiska należało doinstalować pakiet mlflow
<img width="642" height="202" alt="image" src="https://github.com/user-attachments/assets/8064449f-3bbf-47c8-8f92-a92540cf14bb" />
Kolejnym krokiem było uruchomienie serwera
<img width="1915" height="604" alt="image" src="https://github.com/user-attachments/assets/75e4a4e0-05be-4707-813f-5b95973ee247" />

# ZADANIE 2 
## Stworzenie prostego eksperymentu MLflow z logowaniem hiperparametrów i metryk
Eksperyment został wykonany przy użyciu kodu zawartego w sprawozdaniu. Znajduje się on w tym repozytorium
Celem kodu jest utworzenie modelu Decision Tree Classifier, oraz logowaniem jego postępów na MLflow
<img width="1184" height="110" alt="image" src="https://github.com/user-attachments/assets/7dbd930b-d25e-4c05-9cba-1936bc84df45" />

# ZADANIE 3 
## Rejestrowanie i wersjonowanie modelu w MLflow
W zadaniu należało modyfikować parametry modelu, uruchamiać go a następnie korzystając z mlflow monitorować jego wyniki metryk
Zmiana depth = 1
<img width="1182" height="472" alt="image" src="https://github.com/user-attachments/assets/0c14ae61-4887-4d7e-8f52-bb73d156ee9a" />
Zmiana depth = 2
<img width="1202" height="460" alt="image" src="https://github.com/user-attachments/assets/14522896-6adb-491d-81ad-9eb8d1b45c93" />
Zmiana depth = 3
<img width="1178" height="432" alt="image" src="https://github.com/user-attachments/assets/dddb2325-d626-4f76-a637-23415a63da3c" />
## Im większy hiperparametr max_depth tym metryka accuracy bardziej zbliża się do 1. Warto nadmienić że po max_depth=3 wartość accuracy wynosiła 1 co wskazuje na overfit modelu

# ZADANIE 4
## Rejestrowanie i wersjonowanie modelu w MLflow
Zakładka Artifacts modelu z parametrem depth = 1
<img width="1321" height="631" alt="image" src="https://github.com/user-attachments/assets/98653339-bfd1-45f3-a558-1cd36aaa056d" />


Zakładka Artifacts modelu z parametrem depth = 2
<img width="1309" height="619" alt="image" src="https://github.com/user-attachments/assets/f27b7efd-4c6c-48f3-bab2-44323ce0fd25" />


Zakładka Artifacts modelu z parametrem depth = 3
<img width="1340" height="702" alt="image" src="https://github.com/user-attachments/assets/dfc21078-7a1a-423c-8b4d-93c81e387aef" />

# ZADANIE 5
## Wykorzystanie modelu zarejestrowanego w MLflow
W celu sprawdzenia poprawności tego ćwiczenia, dodano skrypt predict.py. Jego celem jest wyjęcie z serwera modelu po określonym id nadanym przez MLflow, następnie sprawdzenie go na fragmencie badanych danych. W tym celu pobrałem do skyptu jeden z utworzonych na MLflow modeli. 
<img width="605" height="390" alt="image" src="https://github.com/user-attachments/assets/224cff24-edde-45a0-bb71-bdf7099cf576" />
<img width="291" height="98" alt="image" src="https://github.com/user-attachments/assets/24eb5ae2-bd5f-4ca8-a19d-c5bbcc9e5315" />

# WNIOSKI 
-Narzędzie MLflow jest świetnym rozwiązaniem w przypadku gdy chcemy zautomatyzować proces tworzenia wersji utworzonych modeli 
-MLflow jest bardzo intuicyjne w obsłudze dzięki jego dashboardowi
-Serwer MLflow postawiony na dedykowanej maszynie może zabezpieczyć nas przed utratą utworzonych modeli 

