# Install python
FROM python:3.11.6

# Install dependencies
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install -e .

# Install fonts
RUN apt-get update -y
RUN wget http://ftp.uk.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-mscorefonts-installer_3.8.1_all.deb
RUN dpkg -i ttf-mscorefonts-installer_3.8.1_all.deb || true
RUN apt --fix-broken install -y
RUN rm ttf-mscorefonts-installer_3.8.1_all.deb
RUN rm ~/.cache/matplotlib -rf

CMD ["/bin/bash"]