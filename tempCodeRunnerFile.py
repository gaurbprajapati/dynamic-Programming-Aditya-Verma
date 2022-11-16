import keyboard as key
key.wait("esc")
a = """
package q11067;

public class CompareArrays {
/** Compare lengths and elements of the arr1 and arr2 are equal or not
* 
* 
* 
* @return result
*/ 

public boolean compareArrays(int[] arr1, int[] arr2) {

boolean ans=(arr1.length==arr2.length)?true:false;
int count=0;
if(ans==true){
for(int i=0;i<arr1.length;i++){
if(arr1[i]==arr2[i]){
count++;
}
}
}
if(ans==false || count<arr1.length){
return false;
}else{
return true;
}

//Write your code here


}
}


"""
key.write(a, exact=True, delay=0.05)
