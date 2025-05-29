const mudar = document.getElementById("mudar")
        const confirmar = document.getElementById('confirmar')
        const mae = document.getElementById('mae')
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
        ["Mônaco", "Nauru", "Vaticano", "San Marino", "Qual é o menor país do mundo em área territorial?"],
        ["1776", "1804", "1789", "1799", "Em que ano ocorreu a Revolução Francesa?"],
        ["Japão", "Alemanha", "Austrália", "Canadá", "Qual desses países não faz parte do G7?"],
        ["Amazonas", "Yangtzé", "Nilo", "Mississippi", "Qual é o rio mais longo do mundo?"],
        ["Auckland", "Christchurch", "Wellington", "Hamilton", "Qual é a capital da Nova Zelândia?"],
        ["Gabriel García Márquez", "Pablo Neruda", "Miguel de Cervantes", "Jorge Luis Borges", "Quem escreveu “Dom Quixote”?"]
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
                    confirmar.innerText = "ent sai daqui corno"
                })
            }
           
        }

        
        
       
        muda_mlk()