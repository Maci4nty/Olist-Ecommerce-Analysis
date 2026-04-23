# Optymalizacja Logistyki E-commerce: Analiza wąskich gardeł doręczeniach (Olist Store)

## 🎯 Cel projektu
Weryfikacja wpływu odległości geograficznej pomiędzy dostawcą a kupującym
na całkowity czas przesyłki oraz identyfikacja trendów zakupowych w czasie


## ⚙️ Opis procesu (Data Pipeline)
Projekt oparty na zbiorze danych pobranych z Kaggle, obejmujący ok. 100 tys zamówień.
Przeprowadziłem pełen proces analityczny typu **End-to-End**:
1. **ETL** - ekstrakcja danych z plików CSV i ich transformacja w Pythonie.
2. **Storage** - budowa relacyjnej bazy w SQLite i zautomatyzowane zasilenie jej przetworzonymi danym
3. **Data Modeling** - opracowanie własnych miar (np. flaga lokalizacji) przy pomocy zapytań SQL
4. **BI** - budowa interaktywnego dashboardu z wnioskami biznesowymi


## 🧠 Kompetencje analityczne:
* **ETL** - budowa rurociągów danych wraz z automatyzacją procesów
* **Czyszczenie i modelowanie danych** - obsługa brakujących wartości, rzutowanie typów
* **Analiza statystyczna** - interpretacja korelacji i trendów czasowych
* **Storytelling danych** - przełożenie danych na wnioski biznesowe

## 🛠️ Technologie: 
* **SQL** (CTE, agregacje, złożone zapytania)
* **Python** (Pandas, SQLite, Seaborn, Matplotlib) 
* **PowerBi** (Power Query, Wizualizacja)

## 📈 Kluczowe wnioski:
* **Geografia dostaw:** Potwierdzenie wpływu logistyki międzyregionalnej na czas doręczenia.
Przesyłki między stanami trwają o **87% dłużej**, niż dostawy lokalne

* **Trendy czasowe:** Wzmożona aktywność zakupowa pod koniec tygodnia pozwalająca
na lepsze planowanie zasobów magazynowych