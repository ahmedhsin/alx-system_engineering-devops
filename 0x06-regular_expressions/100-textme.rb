#!/usr/bin/env ruby
str1 =  ARGV[0].scan(/from:(\+\d+)?(\w+)/).join
str2 =  ARGV[0].scan(/to:(\+\d+)?(\w+)/).join
str3 =  ARGV[0].scan(/flags:([-\d:]+)/).join
puts "#{str1},#{str2},#{str3}"
