echo "Updating container"
sudo apt-get update
sudo apt-get install -y python3-dev libpq-dev

echo "Setting up projects"

echo "Setting up database seed project"
pip install -r database-seed/requirements.txt

echo "Setting up client application (playwright tests)"
pip install -r client/requirements.txt
playwright install
playwright install-deps

echo "Settings up controller applicatino"
pip install -r contoller/requirements.txt
