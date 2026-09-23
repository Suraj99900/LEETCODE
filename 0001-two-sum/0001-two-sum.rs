impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut return_vec: Vec<i32> = Vec::new();
        for index in 0..nums.len(){
            
            for i in index+1..nums.len(){

                let tar :i32 =  nums[index]+nums[i];
                // print!("{:?}: ",nums[index]);
                if(tar == target ){
                    return_vec.push(index.try_into().unwrap());
                    return_vec.push(i.try_into().unwrap());
                    print!(" {:?}: {:?}",index,i);
                    return return_vec;
                }
                
            }
        }

        return return_vec;
    }
}