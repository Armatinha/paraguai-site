import codecs
import re

with codecs.open("index.html", "r", "utf-8") as f:
    text = f.read()

# Header Logo
text = re.sub(
    r'<div class="flex text-white bg-gradient-to-b.*?GEN<span class="text-zinc-400">LABS</span></span>\s*</div>',
    '''<div class="logo flex flex-col justify-center gap-[1px]">
<span class="font-bold text-lg leading-none" style="color: #0B2A4A; letter-spacing: 0.05em;">NOVA ERA</span>
<span class="w-full h-px" style="background-color: #C9A24A;"></span>
<span class="font-medium text-[10px] leading-none" style="color: #C9A24A; letter-spacing: 0.1em;">CONSULTORIA</span>
</div>''',
    text,
    flags=re.DOTALL
)

# Nav links
text = text.replace('Curriculum</a>', 'Benefícios</a>')
text = text.replace('Pricing</a>', 'Como Funciona</a>')
text = text.replace('Mentors</a>', 'Contato</a>')
text = text.replace('Community</a>', '<span class="text-zinc-400">|</span></a>')

text = text.replace('Join waitlist', 'Falar conosco')

# Hero changes
text = text.replace('2k+', '5★')
text = text.replace('<span class="text-zinc-900">New Cohort</span> starts in 3 days', '<span class="text-zinc-900">22mil+</span> clientes atendidos')
text = text.replace('Web3 Finance', 'Sua Residência<br class="hidden md:block" />')
text = text.replace('Mastery Lab', 'Legal no Paraguai')
text = re.sub(
    r'Unlock the potential of decentralized markets\..*?digital asset investors\.',
    'Assessoria completa para brasileiros que desejam viver, investir ou abrir empresa no Paraguai.<br><br>A Nova Era Consultoria acompanha cada etapa do processo com orientação administrativa, suporte local e atendimento em português.',
    text,
    flags=re.DOTALL
)
text = text.replace('Start free trial', 'Falar com Especialista')
text = text.replace('Demo Lesson', 'Como Funciona')
text = text.replace('Duration</p>', 'Processo</p>')
text = text.replace('>8 weeks</p>', '>Acompanhado</p>')
text = text.replace('Level</p>', 'Presença</p>')
text = text.replace('>Intermediate</p>', '>No Paraguai</p>')
text = text.replace('Format</p>', 'Atendimento</p>')
text = text.replace('>Hybrid</p>', '>Em Português</p>')
text = text.replace('Live Market', 'Presença Local')
text = text.replace('>Bitcoin</span>', '>Processo</span>')
text = text.replace('+2.4%', '100% Apv')
text = text.replace('Current Value', 'Acompanhamento')
text = text.replace('$64,231', 'Do Início ao Fim')

# Section 2 - Benefits
text = text.replace('Master the', 'Por que o')
text = text.replace('DeFi Stack', 'Paraguai?')
text = re.sub(
    r'From consensus mechanisms to advanced yield strategies\..*?financial architect\.',
    'O Paraguai oferece um ambiente favorável ao empreendedorismo, com regras claras, incentivos legais e infraestrutura ideal para brasileiros.',
    text,
    flags=re.DOTALL
)

text = text.replace('DAO Governance', 'Processo Simplificado')
text = text.replace('Structure decentralized organizations,\\n                        manage proposals, and implement voting mechanics.', 'Estabeleça sua residência no Paraguai com orientação administrativa adequada e acompanhamento especializado em todo o processo.')

text = text.replace('Tokenomics &amp; Incentives', 'Impostos Reduzidos')
text = text.replace('Design sustainable economic models,\\n                        calculate APY curves, and engineer liquidity mining programs that align stakeholder interests.', 'O Paraguai possui uma das cargas tributárias mais competitivas da América Latina, com impostos simplificados.')

text = text.replace('Smart Contract Logic', 'Proximidade do Brasil')
text = text.replace('Write secure, gas-efficient Solidity\\n                        primitives for AMMs, lending pools, and NFT marketplaces.', 'Fronteira terrestre com o Brasil, voos diretos e enorme facilidade de deslocamento a qualquer momento.')

text = text.replace('On-Chain Analytics', 'Ambiente de Negócios')
text = text.replace('Query complex blockchain data, track\\n                        whale\\n                        movements, and visualize protocol health.', 'Atue no Paraguai em um ambiente favorável ao empreendedorismo, regras claras e suporte aos novos negócios.')

text = text.replace('Protocol Security', 'Rapidez no Processo')
text = text.replace('Identify re-entrancy attacks,\\n                        front-running risks, and implement defensive architecture.', 'Processo organizado e eficiente para obtenção da residência, com etapas claras e acompanhamento até a conclusão.')

# Adding 6th card (Comunidade Brasileira) by duplicating Processo Simplificado
card1 = r'(<!-- Card 1: Governance \(Span 1\) -->.*?</div>\s*</div>)'
match = re.search(card1, text, flags=re.DOTALL)
if match:
    c1 = match.group(1)
    c6 = c1.replace('<!-- Card 1: Governance (Span 1) -->', '<!-- Card 6: Comunidade -->')
    c6 = c6.replace('Processo Simplificado', 'Comunidade Brasileira')
    c6 = c6.replace('Estabeleça sua residência no Paraguai com orientação administrativa adequada e acompanhamento especializado em todo o processo.', 'Mais de 400 mil brasileiros já vivem no Paraguai, com ampla rede de apoio e serviços.')
    text = text.replace(c1, c1 + '\\n' + c6)

process_html = """
</div>
<div class="w-full h-px bg-gradient-to-r from-transparent via-zinc-200 to-transparent mt-16 lg:mt-24 mb-16 lg:mb-24 opacity-60"></div>
<div class="flex flex-col gap-10 z-10 w-full relative mb-12">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 px-1">
        <h2 class="md:text-5xl text-3xl font-medium text-zinc-900 tracking-tighter mb-4">Como <span class="bg-clip-text text-transparent bg-gradient-to-b from-[#0B2A4A] to-neutral-400">Funciona</span></h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 overflow-hidden shadow-zinc-900/5 bg-zinc-200 rounded-[2rem] gap-x-px gap-y-px">
        <div class="group bg-white p-8 hover:bg-zinc-50 transition-colors flex flex-col gap-4">
            <div class="text-[10px] font-bold text-[#C9A24A] tracking-widest uppercase">Etapa 1 de 6</div>
            <h3 class="text-xl tracking-tight font-semibold text-[#0B2A4A] mb-2">Análise de Elegibilidade</h3>
            <p class="text-sm font-medium text-zinc-500 mb-4">Avaliação de perfil e documentação para definir o melhor caminho para obtenção da residência.</p>
            <ul class="text-sm text-zinc-600 space-y-2">
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Revisão completa de documentos</li>
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Verificação de antecedentes</li>
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Plano personalizado de ação</li>
            </ul>
        </div>
        <div class="group bg-white p-8 hover:bg-zinc-50 transition-colors flex flex-col gap-4">
            <div class="text-[10px] font-bold text-[#C9A24A] tracking-widest uppercase">Etapa 2 de 6</div>
            <h3 class="text-xl tracking-tight font-semibold text-[#0B2A4A] mb-2">Apostilamento e Tradução</h3>
            <p class="text-sm font-medium text-zinc-500 mb-4">Orientação sobre apostilamento de Haia no Brasil e tradução juramentada para o espanhol.</p>
            <ul class="text-sm text-zinc-600 space-y-2">
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Apostilamento de Haia no Brasil</li>
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Tradução juramentada oficial</li>
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Validação de certidões</li>
            </ul>
        </div>
        <div class="group bg-white p-8 hover:bg-zinc-50 transition-colors flex flex-col gap-4">
            <div class="text-[10px] font-bold text-[#C9A24A] tracking-widest uppercase">Etapa 3 de 6</div>
            <h3 class="text-xl tracking-tight font-semibold text-[#0B2A4A] mb-2">Viagem ao Paraguai</h3>
            <p class="text-sm font-medium text-zinc-500 mb-4">Agendamos sua viagem e acompanhamos você presencialmente em Ciudad del Este. Cuidamos da logística.</p>
            <ul class="text-sm text-zinc-600 space-y-2">
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Agenda otimizada em Ciudad del Este</li>
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Acompanhamento presencial</li>
                <li class="flex items-center"><div class="w-1.5 h-1.5 rounded-full bg-[#C9A24A] mr-2"></div> Suporte logístico completo</li>
            </ul>
        </div>
    </div>
</div>
</main>
"""

text = re.sub(r'<!-- Top Feature Grid -->.*?</main>', process_html, text, flags=re.DOTALL)

with codecs.open("nova-era-consultoria-part-1.html", "w", "utf-8") as f:
    f.write(text)
