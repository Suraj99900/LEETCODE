impl Solution {
    pub fn reverse(x: i32) -> i32 {

        
        if x > i32::MAX || x < i32::MIN {
            return 0;
        }

        let mut y: i32 = x;
        let mut sumrev: i32 = 0;
        // revers the x value
        while y != 0 {
            let temp = y % 10;
            println!("MAX {:?} MIN {:?}", i32::MAX, i32::MIN);
            println!("sumrev {:?} temp {:?}", sumrev, temp);
            if sumrev > i32::MAX / 10 || (sumrev == i32::MAX / 10 && temp > 7) {
                return 0;
            }
            if sumrev < i32::MIN / 10 || (sumrev == i32::MIN / 10 && temp < -9) {
                return 0;
            }
            sumrev = sumrev * 10 + temp;
            y = y / 10;
        }
        return sumrev;
    }
}