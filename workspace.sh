sudo apt install git -y;
git clone https://github.com/rojasricor/nodejs-rsystfip && git clone https://github.com/rojasricor/api-client-rsystfip;

sudo apt update && sudo apt upgrade -y;

sudo apt install apache2 mariadb-server php -y;

sudo apt install curl -y;

curl -sL https://deb.nodesource.com/setup_19.x | sudo -E bash -;
sudo apt install nodejs -y;

sudo apt install wget -y;

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null;

echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list;
sudo apt update && sudo apt install sublime-text;


## Mysql commands ##
GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'admin' WITH GRANT OPTION;
flush privileges;
exit;

## git

git config --global user.name "rojasricor" && git config --global user.email "rojasricor@gmail.com" && git config --global core.editor "vi" && git config --global color.ui true
