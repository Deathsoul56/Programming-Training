def factorial(n)
    if n == 0 || n == 1
        return 1
    else
        return n * factorial(n - 1)
    end 
end

def fibonacci(n)
    if n == 1 || n == 2
        return 1
    else
        return fibonacci(n - 1) + fibonacci(n - 2)
    end 
end


if __FILE__ == $0
    for i in 0..11
        puts "#{i}! = #{factorial(i)}"
    end 

    for i in 1..11
        puts "fibonacci_{#{i}} = #{fibonacci(i)}"
    end 
end 