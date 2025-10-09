use std::thread
fn main() {
    println!("Hello world ");
    for _ in 0..3{
    thread::spawn(||{
        let mut counter:f64 = 0.00;
        loop {
            counter += 0.001;
            }
        });
    }

        loop{

        }
}
