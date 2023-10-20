#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Product
{
private:
    int cena=0;
    string nazwa;
    friend vector <Product> sortowanie(vector <Product> tab);
public:
    void ustawCene(int cena)
    {
        cena = cena;
    }
    void ustawNazwe(string nazwa)
    {
        nazwa = nazwa;
    }
    int zwrocCene()
    {
        return cena;
    }
    string zwrocNazwe()
    {
        return nazwa;
    }
    Product(int cena1, string nazwa1)
    {
        nazwa = nazwa1;
        cena = cena1;
    }
    Product() 
    {
    }
};
vector <Product> sortowanie(vector <Product> tab)
{
    vector <Product> temp = tab;
    for (int i = 0; i < tab.size() - 1; i++) {
        for (int j = 0; j < (tab.size() - i - 1); j++) {
            if (temp[j].cena > temp[j + 1].cena) {
                Product temp2 = temp[j];
                temp[j] = temp[j + 1];
                temp[j + 1] = temp2;
            }
        }
    }
    return temp;
}


int main()
{
    int cena;
    string nazwa;
    vector <Product> tab;
    for (int i = 0; i < 3; i++)
    {
        cout << "Wpisz nazwe: "; cin >> nazwa; cout << endl;
        cout << "Wpisz cene: "; cin >> cena; cout << endl;
        tab.push_back(Product(cena, nazwa));

    }
    vector <Product> tab1;
    tab1 = sortowanie(tab);
    for (int i = 0; i < 3; i++)
    {
        cout << "Produkt " << i + 1 << ": " << endl;
        cout << "Nazwa " << tab1[i].zwrocNazwe() << endl;
        cout << "Cena " << tab1[i].zwrocCene() << endl;

    }

}