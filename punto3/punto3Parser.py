# Generated from punto3.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,5,1,27,8,1,10,
        1,12,1,30,9,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,39,8,3,10,3,12,3,42,
        9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,5,
        0,1,2,6,0,2,4,6,8,10,0,0,53,0,12,1,0,0,0,2,21,1,0,0,0,4,31,1,0,0,
        0,6,35,1,0,0,0,8,43,1,0,0,0,10,47,1,0,0,0,12,13,3,2,1,0,13,14,5,
        0,0,1,14,1,1,0,0,0,15,16,6,1,-1,0,16,22,3,4,2,0,17,18,5,2,0,0,18,
        19,3,2,1,0,19,20,5,3,0,0,20,22,1,0,0,0,21,15,1,0,0,0,21,17,1,0,0,
        0,22,28,1,0,0,0,23,24,10,2,0,0,24,25,5,1,0,0,25,27,3,2,1,3,26,23,
        1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,
        28,1,0,0,0,31,32,5,4,0,0,32,33,3,6,3,0,33,34,5,5,0,0,34,5,1,0,0,
        0,35,40,3,8,4,0,36,37,5,6,0,0,37,39,3,8,4,0,38,36,1,0,0,0,39,42,
        1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,7,1,0,0,0,42,40,1,0,0,0,43,
        44,5,4,0,0,44,45,3,10,5,0,45,46,5,5,0,0,46,9,1,0,0,0,47,52,5,7,0,
        0,48,49,5,6,0,0,49,51,5,7,0,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,11,1,0,0,0,54,52,1,0,0,0,4,21,28,40,52
    ]

class punto3Parser ( Parser ):

    grammarFileName = "punto3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMERO", "WS" ]

    RULE_programa = 0
    RULE_expresion = 1
    RULE_matriz = 2
    RULE_filas = 3
    RULE_fila = 4
    RULE_elementos = 5

    ruleNames =  [ "programa", "expresion", "matriz", "filas", "fila", "elementos" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMERO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(punto3Parser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(punto3Parser.EOF, 0)

        def getRuleIndex(self):
            return punto3Parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = punto3Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expresion(0)
            self.state = 13
            self.match(punto3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return punto3Parser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a punto3Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(punto3Parser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a punto3Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(punto3Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(punto3Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacion" ):
                listener.enterMultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacion" ):
                listener.exitMultiplicacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacion" ):
                return visitor.visitMultiplicacion(self)
            else:
                return visitor.visitChildren(self)


    class MatrizSolaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a punto3Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matriz(self):
            return self.getTypedRuleContext(punto3Parser.MatrizContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrizSola" ):
                listener.enterMatrizSola(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrizSola" ):
                listener.exitMatrizSola(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrizSola" ):
                return visitor.visitMatrizSola(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = punto3Parser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = punto3Parser.MatrizSolaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.matriz()
                pass
            elif token in [2]:
                localctx = punto3Parser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(punto3Parser.T__1)
                self.state = 18
                self.expresion(0)
                self.state = 19
                self.match(punto3Parser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = punto3Parser.MultiplicacionContext(self, punto3Parser.ExpresionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 23
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 24
                    self.match(punto3Parser.T__0)
                    self.state = 25
                    self.expresion(3) 
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filas(self):
            return self.getTypedRuleContext(punto3Parser.FilasContext,0)


        def getRuleIndex(self):
            return punto3Parser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = punto3Parser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_matriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(punto3Parser.T__3)
            self.state = 32
            self.filas()
            self.state = 33
            self.match(punto3Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(punto3Parser.FilaContext)
            else:
                return self.getTypedRuleContext(punto3Parser.FilaContext,i)


        def getRuleIndex(self):
            return punto3Parser.RULE_filas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilas" ):
                listener.enterFilas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilas" ):
                listener.exitFilas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilas" ):
                return visitor.visitFilas(self)
            else:
                return visitor.visitChildren(self)




    def filas(self):

        localctx = punto3Parser.FilasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.fila()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 36
                self.match(punto3Parser.T__5)
                self.state = 37
                self.fila()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementos(self):
            return self.getTypedRuleContext(punto3Parser.ElementosContext,0)


        def getRuleIndex(self):
            return punto3Parser.RULE_fila

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila" ):
                listener.enterFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila" ):
                listener.exitFila(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila" ):
                return visitor.visitFila(self)
            else:
                return visitor.visitChildren(self)




    def fila(self):

        localctx = punto3Parser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fila)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(punto3Parser.T__3)
            self.state = 44
            self.elementos()
            self.state = 45
            self.match(punto3Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(punto3Parser.NUMERO)
            else:
                return self.getToken(punto3Parser.NUMERO, i)

        def getRuleIndex(self):
            return punto3Parser.RULE_elementos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementos" ):
                listener.enterElementos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementos" ):
                listener.exitElementos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementos" ):
                return visitor.visitElementos(self)
            else:
                return visitor.visitChildren(self)




    def elementos(self):

        localctx = punto3Parser.ElementosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elementos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(punto3Parser.NUMERO)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 48
                self.match(punto3Parser.T__5)
                self.state = 49
                self.match(punto3Parser.NUMERO)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




