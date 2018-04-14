# Generated from grammars/uciPurdueUnix.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\r")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\5\4\27\n\4\3\5\3\5\3\5")
        buf.write("\7\5\34\n\5\f\5\16\5\37\13\5\3\6\3\6\3\6\7\6$\n\6\f\6")
        buf.write("\16\6\'\13\6\3\7\3\7\7\7+\n\7\f\7\16\7.\13\7\3\7\3\7\3")
        buf.write("\7\2\2\b\2\4\6\b\n\f\2\2/\2\16\3\2\2\2\4\22\3\2\2\2\6")
        buf.write("\26\3\2\2\2\b\30\3\2\2\2\n \3\2\2\2\f(\3\2\2\2\16\17\7")
        buf.write("\3\2\2\17\20\7\5\2\2\20\21\7\4\2\2\21\3\3\2\2\2\22\23")
        buf.write("\7\7\2\2\23\5\3\2\2\2\24\27\7\6\2\2\25\27\5\2\2\2\26\24")
        buf.write("\3\2\2\2\26\25\3\2\2\2\27\7\3\2\2\2\30\31\5\4\3\2\31\35")
        buf.write("\7\r\2\2\32\34\5\6\4\2\33\32\3\2\2\2\34\37\3\2\2\2\35")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\t\3\2\2\2\37\35\3\2\2\2 ")
        buf.write("%\5\b\5\2!\"\7\13\2\2\"$\5\b\5\2#!\3\2\2\2$\'\3\2\2\2")
        buf.write("%#\3\2\2\2%&\3\2\2\2&\13\3\2\2\2\'%\3\2\2\2(,\7\t\2\2")
        buf.write(")+\5\n\6\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3")
        buf.write("\2\2\2.,\3\2\2\2/\60\7\n\2\2\60\r\3\2\2\2\6\26\35%,")
        return buf.getvalue()


class uciPurdueUnixParser ( Parser ):

    grammarFileName = "uciPurdueUnix.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'**SOF**'", "'**EOF**'", 
                     "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "TEXT", 
                      "WORD", "WHITESPACE", "SESS_START", "SESS_END", "PIPE", 
                      "OPTION", "OPTIONS" ]

    RULE_files = 0
    RULE_utility = 1
    RULE_argument = 2
    RULE_command = 3
    RULE_pipeline = 4
    RULE_session = 5

    ruleNames =  [ "files", "utility", "argument", "command", "pipeline", 
                   "session" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUMBER=3
    TEXT=4
    WORD=5
    WHITESPACE=6
    SESS_START=7
    SESS_END=8
    PIPE=9
    OPTION=10
    OPTIONS=11

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FilesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(uciPurdueUnixParser.NUMBER, 0)

        def getRuleIndex(self):
            return uciPurdueUnixParser.RULE_files

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiles" ):
                listener.enterFiles(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiles" ):
                listener.exitFiles(self)




    def files(self):

        localctx = uciPurdueUnixParser.FilesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_files)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(uciPurdueUnixParser.T__0)
            self.state = 13
            self.match(uciPurdueUnixParser.NUMBER)
            self.state = 14
            self.match(uciPurdueUnixParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UtilityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(uciPurdueUnixParser.WORD, 0)

        def getRuleIndex(self):
            return uciPurdueUnixParser.RULE_utility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUtility" ):
                listener.enterUtility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUtility" ):
                listener.exitUtility(self)




    def utility(self):

        localctx = uciPurdueUnixParser.UtilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_utility)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(uciPurdueUnixParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(uciPurdueUnixParser.TEXT, 0)

        def files(self):
            return self.getTypedRuleContext(uciPurdueUnixParser.FilesContext,0)


        def getRuleIndex(self):
            return uciPurdueUnixParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = uciPurdueUnixParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            token = self._input.LA(1)
            if token in [uciPurdueUnixParser.TEXT]:
                self.state = 18
                self.match(uciPurdueUnixParser.TEXT)

            elif token in [uciPurdueUnixParser.T__0]:
                self.state = 19
                self.files()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def utility(self):
            return self.getTypedRuleContext(uciPurdueUnixParser.UtilityContext,0)


        def OPTIONS(self):
            return self.getToken(uciPurdueUnixParser.OPTIONS, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uciPurdueUnixParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(uciPurdueUnixParser.ArgumentContext,i)


        def getRuleIndex(self):
            return uciPurdueUnixParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = uciPurdueUnixParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.utility()
            self.state = 23
            self.match(uciPurdueUnixParser.OPTIONS)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uciPurdueUnixParser.T__0 or _la==uciPurdueUnixParser.TEXT:
                self.state = 24
                self.argument()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PipelineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uciPurdueUnixParser.CommandContext)
            else:
                return self.getTypedRuleContext(uciPurdueUnixParser.CommandContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(uciPurdueUnixParser.PIPE)
            else:
                return self.getToken(uciPurdueUnixParser.PIPE, i)

        def getRuleIndex(self):
            return uciPurdueUnixParser.RULE_pipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipeline" ):
                listener.enterPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipeline" ):
                listener.exitPipeline(self)




    def pipeline(self):

        localctx = uciPurdueUnixParser.PipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.command()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uciPurdueUnixParser.PIPE:
                self.state = 31
                self.match(uciPurdueUnixParser.PIPE)
                self.state = 32
                self.command()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SessionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SESS_START(self):
            return self.getToken(uciPurdueUnixParser.SESS_START, 0)

        def SESS_END(self):
            return self.getToken(uciPurdueUnixParser.SESS_END, 0)

        def pipeline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uciPurdueUnixParser.PipelineContext)
            else:
                return self.getTypedRuleContext(uciPurdueUnixParser.PipelineContext,i)


        def getRuleIndex(self):
            return uciPurdueUnixParser.RULE_session

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSession" ):
                listener.enterSession(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSession" ):
                listener.exitSession(self)




    def session(self):

        localctx = uciPurdueUnixParser.SessionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_session)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(uciPurdueUnixParser.SESS_START)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uciPurdueUnixParser.WORD:
                self.state = 39
                self.pipeline()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(uciPurdueUnixParser.SESS_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





