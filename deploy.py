# WOW 키캡 룰렛 배포: 08 폴더의 빌드 html → index.html(+공유 메타) — python deploy.py "<08 폴더 파일 이름>"
import pathlib, sys
D = pathlib.Path(r"c:/Users/KUH/OneDrive - 건국대학교병원/★김희준 업무자료★/★0. WoW Together/05_캠페인위크·팝업/08_WOW퀴즈&WOW룰렛")
META = '''<meta name="robots" content="noindex,nofollow">
<meta property="og:title" content="WOW 키캡 룰렛 — WOW Together">
<meta property="og:description" content="레버를 당기면 일·서로·변화 문장 키캡 3개!">
<meta property="og:image" content="https://kuhedu.github.io/wowroulette/og.png">
<meta property="og:type" content="website">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="WOW 룰렛">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="icon" href="icon-192.png">
'''
s = (D / sys.argv[1]).read_text(encoding='utf-8')
assert s.count('<title>') == 1
pathlib.Path(__file__).with_name('index.html').write_text(s.replace('<title>', META + '<title>', 1), encoding='utf-8')
print('index.html <-', sys.argv[1])
