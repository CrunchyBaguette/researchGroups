# researchGroups


## Odpalanie środowiska z dockerem

Żeby odpalić to za pomocą docker compose to wystarczy w terminalu w folderze repo (czyli researchGroups) odpalić `docker compose up`

To postawi wszystkie kontenery razem z UI i Django i Postgresem. Będzie to też najnowsza wersja bo te obrazy są budowane na podstawie tego co jest w repo a nie np dla poszczególnego tagu czy coś.

Jeśli nie chcecie odpalać wszystkiego za każdym razem żeby przebudowywał obrazy to można zawsze odpalić na przykład tylko postgresa bo to jedyne co może zostać odpalone tylko przez dockera.

Wystarczy odpalić `docker run --name postgres -e POSTGRES_DB=backend -e POSTGRES_PASSWORD=pleasechangeme -p 5432:5432 -d` ale to jest długa komenda więć łatwiej jest odaplić po prostu jeden serwis z compose.

Można to zrobić tak: `docker compose up postgres`

Aby zatrzymać kontener `docker compose down` a żeby przy zatrzymywaniu usunąć dane to `docker compose down -v`