FROM openjdk:slim
COPY --from=python:3.8 / /
COPY . ./ui
WORKDIR /ui
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN ALLURE_VERSION=2.13.9 \
    && wget -qO /tmp/allure-"$ALLURE_VERSION".tgz https://github.com/allure-framework/allure2/releases/download/"$ALLURE_VERSION"/allure-"$ALLURE_VERSION".tgz \
    && tar -xf /tmp/allure-"$ALLURE_VERSION".tgz --directory=/opt/ \
    && ln -s /opt/allure-"$ALLURE_VERSION"/bin/allure /usr/bin/allure