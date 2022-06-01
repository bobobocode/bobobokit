# Scaffold

## electron

    npm init

## Maven

    mvn package -DskipTests
    mvn archetype:generate -DgroupId=<name> -DartifactId=<name> -DinteractiveMode=false
    mvn test -Dtest=MyClassTest#*test*
    mvn spring-boot:run
    mvn dependency:tree
    mvn exec:java -Dexec.mainClass="com.vineetmanohar.module.Main"

## Spring

    spring init -dweb,data-jpa,h2,thymeleaf --build maven demo

## Python

    python setup.py sdist build
    twine upload dist/*
