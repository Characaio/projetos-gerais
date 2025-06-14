 const mudar = document.getElementById("mudar")
        const confirmar = document.getElementById('confirmar')
        const mae = document.getElementById('mae')
        const mae2 = document.getElementById('mae2')
        let acertos = 0
        let erros = 0
        // let coisas = [
        //     ["Lady Gaga", "kate perry","taylor swift","will smith","quem é a melhor diva pop?"],//pergunta,alternativa1,alternativa2,alternativa3,alternativa4
        //     ["isabela ribeiro", "isabela","todas mencionadas","isabela ribeiro silva","quem que o caio ama?"],
        //     ['caio henrique','caio','todos mencionados','caio henrique caetano da silva gomes', 'quem a isa ama?'],
        //     ['evil farm game','terraria','stardew valley','minecraft','qual é o melhor jogo de fazenda?'],
        //     ['2010','1970','2001','2009','que ano Minecraft foi lançado?'],
        //     ['Ocarina of Time','Skyward Sword','Twilight Princess','Majoras mask', 'qual foi o melhor Zelda de todos?']
        // ]
        let coisas = [
            ["Minecraft", "Stardew Valley","Terraria","block game","Qual jogo é conhecido como 'minecraft 2D'?"],
            ["Terraria","Raft","Subnautica","The Escapists","Qual jogo temos o 'leviatã ceifador'?"],
            ["Thor o Urso", "Rex o Cachorro","Daisy a Coelha","Mika a Rata","Qual era o animal e o nome do estimação do Doom Slayer?"],
            ["Kris", "Spamton E spamton","Spamnton G Spamton","Mike...","Quem quer ser um [BIG SHOT]?"],
            ["Uma Vaca", "Um Porco","Uma Galinha","Uma Ovelha","Qual é a logo do Stardew Valley?"],
            ["Kamarov", "John 'Soap' Mactavish","Gaz","Capitão John Price","A frase 'mudar para sua pistola é sempre mais rapido do que recarregar' é de quem?"]
        ]

        let escolha = -1
        socorro = `
        <p> reiniciar o quiz? </p>
        <button id ="sim">sim</button>
        <button id ="nao">nao</button>
        `
        function muda_mlk(){
            if (escolha < coisas.length-1){
                escolha += 1
                mae.innerHTML = `
                <div id = "silva1">
                    <div>
                        <button id = "primeiro"> opção 1</button>
                    </div>
                    
                    <div>
                        <button  id = "terceiro"> opção 3</button>
                    </div>
                </div>
                <div id = silva2>
                    <div>
                        <button  id = "segundo"> opção 2</button>
                    </div>
                    <div>
                        <button  id = "quarto"> opção 4</button>
                    </div>
                </div>
                
                `
                const primeiro = document.getElementById("primeiro")
                const segundo = document.getElementById("segundo")
                const terceiro = document.getElementById("terceiro")
                const quarto = document.getElementById("quarto")
                const pergunta = document.getElementById("pergunta")
                primeiro.innerText = coisas[escolha][0]
                segundo.innerText = coisas[escolha][1]
                terceiro.innerText = coisas[escolha][2]
                quarto.innerText = coisas[escolha][3]
                pergunta.innerText = coisas[escolha][4]
                primeiro.addEventListener('click', () =>{
                if (primeiro.textContent == coisas[escolha][2]){
                    acertos += 1
                } else{
                    erros += 1
                }
                muda_mlk()
                console.log(coisas[escolha][2])
                
                })
                segundo.addEventListener('click', () =>{
                    if (segundo.textContent == coisas[escolha][2]){
                        acertos += 1
                    } else{
                        erros += 1
                    }
                    muda_mlk()
                    console.log(coisas[escolha][2])
                })
                terceiro.addEventListener('click', () =>{
                    if (terceiro.textContent == coisas[escolha][2]){
                        acertos += 1
                    } else{
                        erros += 1
                    }
                    muda_mlk()
                    console.log(coisas[escolha][2])
                })
                quarto.addEventListener('click', () =>{
                    if (quarto.textContent == coisas[escolha][2]){
                        acertos += 1
                    } else{
                        erros += 1
                    }
                    muda_mlk()
                    console.log(coisas[escolha][2])
                })
                }
            else{
                console.log('acabou');
                mae.innerHTML = ''
                pergunta.innerText = 'você acertou ' + acertos + " e errou " + erros
                confirmar.innerHTML = socorro

                const sim = document.getElementById('sim')
                const nao = document.getElementById('nao')
                sim.addEventListener('click', () =>{
                    console.log('oi');
                    
                    escolha = -1
                    acertos = 0
                    erros = 0
                    confirmar.innerHTML = ''
                    muda_mlk()

                })
                nao.addEventListener("click", () =>{
                    window.location.replace("../paginainicial.html")
                })
            }
           
        }

        
        
       
        muda_mlk()