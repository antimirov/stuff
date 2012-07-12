-module(p22).
-compile(export_all).
-export([start/0]).



start() ->

    {ok, BinData} = file:read_file("p22_names.txt"),

    {ok,Words0} = regexp:split( string:strip( binary_to_list(BinData) ), "," ),
    Words = lists:sort(lists:map(fun(X) -> {ok, Clean, _} = regexp:gsub(X,"\"",""), Clean end, Words0)),

    CountSum = fun(X) ->
            lists:sum([Letter-64 || Letter <- X])
        end,

    SumPair = lists:zip(lists:map(CountSum, Words),lists:seq(1,length(Words))),

    TotalSumFunc = fun({LSum,Num}) ->
            LSum*Num
        end,

    TotalSum = lists:sum(lists:map(TotalSumFunc, SumPair)),

    io:format("~nTotal sum: ~p~n", [TotalSum]).
