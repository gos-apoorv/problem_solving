func canConstruct(ransomNote string, magazine string) bool {
    
    if len(magazine) < len(ransomNote){
        return false
    }
    
    
    var charMap map[rune]int = make(map[rune]int)
    
    for _,v := range magazine{
        if cnt,ok:= charMap[v];ok{
            charMap[v] = cnt +1
        } else {
            charMap[v] = 1
        } 
    }
    
    fmt.Println(charMap)
    
    for _,j := range  ransomNote{
        if cnt,ok:= charMap[j];ok && cnt >= 1{
            charMap[j] = cnt - 1
        } else {
            return false
        } 
            
    fmt.Println(j, charMap)
    }
    
    return true
    
}