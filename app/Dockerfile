FROM ubuntu

MAINTAINER frankschmitt@gmx.de

RUN mkdir /opt/tomcat/

WORKDIR /opt/tomcat
RUN apt-get update \
    && apt-get install -y openjdk-8-jdk \
    && apt-get install -y curl \
    && rm -rf /apt/cache/sources.list
RUN java -version

RUN curl -O https://downloads.apache.org/tomcat/tomcat-8/v8.5.82/bin/apache-tomcat-8.5.82.tar.gz
RUN tar xvfz apache*.tar.gz
RUN mv apache-tomcat-8.5.82/* /opt/tomcat/.

WORKDIR /opt/tomcat/webapps
RUN curl -O -L https://github.com/AKSarav/SampleWebApp/raw/master/dist/SampleWebApp.war

EXPOSE 8080

CMD ["/opt/tomcat/bin/catalina.sh", "run"]
