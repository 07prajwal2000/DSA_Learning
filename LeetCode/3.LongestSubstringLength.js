function LongestSubstring(s) {
    if (s.length === 0) return 0;
    let left = 0;
    let count = 1;
    let charMap = {};

    charMap[s[0]] = true;
    
    for (let right = 1; right < s.length; right++) {

        if ( charMap[ s[right] ] !== undefined ) {
            delete charMap[ s[right] ];
            
            while (left <= right) {
                if ( charMap[ s[left] ] !== undefined ) {
                    delete charMap[ s[right] ];
                    let localCount = right - left + 1;
                    count = localCount > count ? localCount : count;
                }

                left++;
            }
        }
        
        charMap[ s[right] ] = true;

    }
    return count;
}


// console.log(LongestSubstring("abcabcbba"));
// console.log(LongestSubstring("pwwkew"));
// console.log(LongestSubstring("bbbbb"));
console.log(LongestSubstring("au"));