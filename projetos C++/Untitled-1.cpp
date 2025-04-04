#include <iostream>


using namespace std;



int main()
{
    /*
    boolean: 1 byte
    char: 1 byte
    int: 2 ou 4 bytes
    float: 4 bytes
    double 8 bytes
    */

    // float e double tem o mesmo proposito, mas double são mais precisos

    /*
    	++  Increment	Increases the value of a variable by 1	++x	
        --	Decrement	Decreases the value of a variable by 1	--x 
    */

    /*
        && and
        || or
        !  not
    */

    // você pode usar valores ASCII com as variaveis char para usar certos caracteres

    // variaveis do tipo char segura APENAS UM CARACTERE
    int idade = 15;
    const int me_salve_as = 15;
    int x,y,z;
    double altura;
    string nota;
    string nome;
    // eu não sei QUE DESGRAÇA eu estou FAZENDO
    /*eu quero cometer
    um crime contra
    uma creche
    e eu não vou me arrepender*/

    cout << "coloque sua idade: \n";
    cin >> idade;

    cout << "coloque sua altura: \n";
    cin >> altura;

    cout << "coloque sua nota: \n";
    cin >> nota;

    cout << "escreva seu nome completo: \n";
    /* i con.ignore é usado para limpar o buffer de input, no nosso caso, limpamos o "\n", em geral isso não é necessario
    mas em nosso caso que temos que usar o getline(), temos que limpar se não o getline ira ler o "\n" inves do nosso input
    isso se da pois o getline le a linha inteira, e se ela ler uma linha que esta com um "\n" ela ira ficar vazia*/
    // USE O CIN.IGNORE APENAS SE VOCÊ USAR O \N
    cin.ignore(); 
    getline(cin,nome);

    x = y = z = 5;

    cout << "im learning c++\n";
    cout << "meu nome é " << nome << ", tenho " << idade << "anos, tenho " << altura << " metros de atura, eu tirei nota " << nota << "\n";
    cout << "o tamanho do seu nome é de: " << nome.length() << "\n";

    

    cout << x << ' ' << y << ' ' << z << ' ' << '\n';
    cout << "hello world";

    return 0;
}
