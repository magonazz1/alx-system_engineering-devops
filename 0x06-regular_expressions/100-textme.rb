#!/usr/bin/env ruby


def retrieve_info(logs)
  sender_info = logs[/from:([\w\+\d]+|w+\s\w+)/, 1]
  receiver_info = logs[/to:([\w\+\d]+|w+\s\w+)/, 1]
  flags_present = logs[/flags:(\S+)/, 1]

  "#{sender_info},#{receiver_info},#{flags_present}"
end

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <logs>"
  exit(1)
end

logs = ARGV[0]
output = retrieve_info(logs)
puts(output)
