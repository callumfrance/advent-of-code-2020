import qualified Data.HashMap.Strict as M
import System.IO  
import Control.Monad

main = do
    let fileName = "./src/input.txt"
    contents <- readFile fileName
    putStrLn contents

f :: [String] -> [Int]
f = map read
