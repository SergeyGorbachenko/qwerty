import webbrowser, json, os, speech_recognition, pyttsx3, smtplib
from flask import Flask, render_template, request, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

app = Flask(__name__, static_folder='templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/voice', methods=['POST'])
def contact():
    try:
        sr = speech_recognition.Recognizer()
        sr.pause_threshold = 0.5

        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
        if query == "директор": 

            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Скажите комментарий для директора')
            engine.runAndWait()

            sr = speech_recognition.Recognizer()
            sr.pause_threshold = 0.5

            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query_com = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                com = query_com

            with open('templates/info.json') as f:
                data = json.load(f)
            mail = data['email']
            recip = data['director']
            floor = data['floor']
            room = data['room']


            server = 'smtp.mail.ru'
            user = 'python.django@bk.ru'
            password = 'We4tnWeh34BZKfiCpKX2'

            recipients = [recip]
            
            sender = 'python.django@bk.ru'
            subject = 'Voice Assistent'
            text_adr = ('Получено из ' + room + ' кабинета на ' + floor + ' этаже')
            text_send = 'Отправлено ' + mail
            text = text_adr + '<h1>' + query + ':' + ' ' + com + '</h1>' + text_send
            html = '<html><head></head><body><p>' + text + '</p></body></html>'

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'Voice assistent Avatar <' + sender + '>'
            msg['To'] = ', '.join(recipients)
            msg['Reply-To'] = sender
            msg['Return-Path'] = sender
            msg['X-Mailer'] = 'Python/' + (python_version())

            part_text = MIMEText(text, 'plain')
            part_html = MIMEText(html, 'html')
            msg.attach(part_text)
            msg.attach(part_html)

            mail = smtplib.SMTP_SSL(server)
            mail.login(user, password)
            mail.sendmail(sender, recipients, msg.as_string())
            mail.quit()


            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Сообщение успешно отправлено')
            engine.runAndWait()

        elif query == "медсестра":
            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Скажите комментарий для медсестры')
            engine.runAndWait()


            sr = speech_recognition.Recognizer()
            sr.pause_threshold = 0.5

            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query_com = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                com = query_com

            with open('templates/info.json') as f:
                data = json.load(f)
            mail = data['email']
            recip = data['med']
            floor = data['floor']
            room = data['room']


            server = 'smtp.mail.ru'
            user = 'python.django@bk.ru'
            password = 'We4tnWeh34BZKfiCpKX2'

            recipients = [recip]

            sender = 'python.django@bk.ru'
            subject = 'Voice Assistent'
            text_adr = ('Получено из ' + room + ' кабинета на ' + floor + ' этаже')
            text_send = 'Отправлено ' + mail
            text = text_adr + '<h1>' + query + ':' + ' ' + com + '</h1>' + text_send
            html = '<html><head></head><body><p>' + text + '</p></body></html>'

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'Voice assistent Avatar <' + sender + '>'
            msg['To'] = ', '.join(recipients)
            msg['Reply-To'] = sender
            msg['Return-Path'] = sender
            msg['X-Mailer'] = 'Python/' + (python_version())

            part_text = MIMEText(text, 'plain')
            part_html = MIMEText(html, 'html')
            msg.attach(part_text)
            msg.attach(part_html)

            mail = smtplib.SMTP_SSL(server)
            mail.login(user, password)
            mail.sendmail(sender, recipients, msg.as_string())
            mail.quit()


            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Сообщение успешно отправлено')
            engine.runAndWait()

        elif query == "системный администратор":
            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Скажите комментарий для системного администратора')
            engine.runAndWait()


            sr = speech_recognition.Recognizer()
            sr.pause_threshold = 0.5

            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query_com = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                com = query_com

            with open('templates/info.json') as f:
                data = json.load(f)
            mail = data['email']
            recip = data['admin']
            floor = data['floor']
            room = data['room']


            server = 'smtp.mail.ru'
            user = 'python.django@bk.ru'
            password = 'We4tnWeh34BZKfiCpKX2'

            recipients = [recip]

            sender = 'python.django@bk.ru'
            subject = 'Voice Assistent'
            text_adr = ('Получено из ' + room + ' кабинета на ' + floor + ' этаже')
            text_send = 'Отправлено ' + mail
            text = text_adr + '<h1>' + query + ':' + ' ' + com + '</h1>' + text_send
            html = '<html><head></head><body><p>' + text + '</p></body></html>'

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'Voice assistent Avatar <' + sender + '>'
            msg['To'] = ', '.join(recipients)
            msg['Reply-To'] = sender
            msg['Return-Path'] = sender
            msg['X-Mailer'] = 'Python/' + (python_version())

            part_text = MIMEText(text, 'plain')
            part_html = MIMEText(html, 'html')
            msg.attach(part_text)
            msg.attach(part_html)

            mail = smtplib.SMTP_SSL(server)
            mail.login(user, password)
            mail.sendmail(sender, recipients, msg.as_string())
            mail.quit()


            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Сообщение успешно отправлено')
            engine.runAndWait()

        elif query == "завхоз":
            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Скажите комментарий для завхоза')
            engine.runAndWait()


            sr = speech_recognition.Recognizer()
            sr.pause_threshold = 0.5

            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query_com = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                com = query_com

            with open('templates/info.json') as f:
                data = json.load(f)
            mail = data['email']
            recip = data['zav']
            floor = data['floor']
            room = data['room']


            server = 'smtp.mail.ru'
            user = 'python.django@bk.ru'
            password = 'We4tnWeh34BZKfiCpKX2'

            recipients = [recip]

            sender = 'python.django@bk.ru'
            subject = 'Voice Assistent'
            text_adr = ('Получено из ' + room + ' кабинета на ' + floor + ' этаже')
            text_send = 'Отправлено ' + mail
            text = text_adr + '<h1>' + query + ':' + ' ' + com + '</h1>' + text_send
            html = '<html><head></head><body><p>' + text + '</p></body></html>'

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'Voice assistent Avatar <' + sender + '>'
            msg['To'] = ', '.join(recipients)
            msg['Reply-To'] = sender
            msg['Return-Path'] = sender
            msg['X-Mailer'] = 'Python/' + (python_version())

            part_text = MIMEText(text, 'plain')
            part_html = MIMEText(html, 'html')
            msg.attach(part_text)
            msg.attach(part_html)

            mail = smtplib.SMTP_SSL(server)
            mail.login(user, password)
            mail.sendmail(sender, recipients, msg.as_string())
            mail.quit()


            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Сообщение успешно отправлено')
            engine.runAndWait()

        elif query == "охранник":
            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Скажите комментарий для охранника')
            engine.runAndWait()


            sr = speech_recognition.Recognizer()
            sr.pause_threshold = 0.5

            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query_com = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                com = query_com

            with open('templates/info.json') as f:
                data = json.load(f)
            mail = data['email']
            recip = data['sec']
            floor = data['floor']
            room = data['room']


            server = 'smtp.mail.ru'
            user = 'python.django@bk.ru'
            password = 'We4tnWeh34BZKfiCpKX2'

            recipients = [recip]

            sender = 'python.django@bk.ru'
            subject = 'Voice Assistent'
            text_adr = ('Получено из ' + room + ' кабинета на ' + floor + ' этаже')
            text_send = 'Отправлено ' + mail
            text = text_adr + '<h1>' + query + ':' + ' ' + com + '</h1>' + text_send
            html = '<html><head></head><body><p>' + text + '</p></body></html>'

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'Voice assistent Avatar <' + sender + '>'
            msg['To'] = ', '.join(recipients)
            msg['Reply-To'] = sender
            msg['Return-Path'] = sender
            msg['X-Mailer'] = 'Python/' + (python_version())

            part_text = MIMEText(text, 'plain')
            part_html = MIMEText(html, 'html')
            msg.attach(part_text)
            msg.attach(part_html)

            mail = smtplib.SMTP_SSL(server)
            mail.login(user, password)
            mail.sendmail(sender, recipients, msg.as_string())
            mail.quit()


            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Сообщение успешно отправлено')
            engine.runAndWait()

        
        else:
            engine = pyttsx3.init()
            ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
            engine.setProperty('voice', ru_voice_id)
            engine.say('Скажите четко и громко должность, а я постараюсь вас понять')
            engine.runAndWait()
            return render_template('main.html')

        return render_template('main.html')
    except:
        engine = pyttsx3.init()
        ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
        engine.setProperty('voice', ru_voice_id)
        engine.say('Произошла ошибка , попробуйте перезапустить приложение или перезапишите данные в меню настроек')
        engine.runAndWait()
        return render_template('main.html')

@app.route('/reg_handler', methods=['POST'])
def reg():
    email = request.form['email']
    floor = request.form['floor']
    room = request.form['room']
    director = request.form['director']
    zav = request.form['zav']
    admin = request.form['admin']
    med = request.form['med']
    sec = request.form['sec']


    info = {
        'email': email,
        'floor': floor,
        'room': room,
        'director': director,
        'zav': zav,
        'admin': admin,
        'med': med,
        'sec': sec,
    }

    with open('templates/info.json', 'w', encoding='utf-8') as file:
        json.dump(info, file, indent=4, ensure_ascii=False)
    
    return redirect("http://127.0.0.1:8080/#tab_02", code=302)


if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:8080")
    app.run(port=8080, host='127.0.0.1')
    