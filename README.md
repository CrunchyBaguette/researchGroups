# researchGroups


## Odpalanie środowiska z dockerem

Żeby odpalić to za pomocą docker compose to wystarczy w terminalu w folderze repo (czyli researchGroups) odpalić `docker compose up`

To postawi wszystkie kontenery razem z UI i Django i Postgresem. Będzie to też najnowsza wersja bo te obrazy są budowane na podstawie tego co jest w repo a nie np dla poszczególnego tagu czy coś.

Jeśli nie chcecie odpalać wszystkiego za każdym razem żeby przebudowywał obrazy to można zawsze odpalić na przykład tylko postgresa bo to jedyne co może zostać odpalone tylko przez dockera.

Wystarczy odpalić `docker run --name postgres -e POSTGRES_DB=backend -e POSTGRES_PASSWORD=pleasechangeme -p 5432:5432 -d` ale to jest długa komenda więć łatwiej jest odaplić po prostu jeden serwis z compose.

Można to zrobić tak: `docker compose up postgres`

Aby zatrzymać kontener `docker compose down` a żeby przy zatrzymywaniu usunąć dane to `docker compose down -v`

Dodałem jeszcze żeby pgadmin był w przeglądarce jest on na porcie 5050 czyli `localhost:5050` i będzię. Tylko wszystko to podzieliłem na profile żeby nie trzeba było wybierać co chce się uruchamiać

Czyli jak chcecie odpalić pgadmin to zaczyna się `docker compose --profile dev up -d` to postawi tylko bazę i pgAdmin w kontenerach. Backend i front trzeba będzie samemu postawić.

`docker compose --profile prod up -d` postawi wszystko oprócz pgadmina 

`docker compose --profile debug up -d` postawi wszystkie kontenery.

Żeby zamknąć kontenery uruchomione w ten sposób to trzeba wpisać `docker compose -profile profil down` bo samo `docker compose donw` nie zadziała

Oczywiście można dodać na końcu -v aby usunąć dane.

Dane do logowania do pgAdmin to admin@example.com i hasło admin