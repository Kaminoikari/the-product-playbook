# ✏️ 커스텀 모드 단계 시퀀스

> 이 파일은 커스텀 모드의 권위 있는 단계 정의입니다. SKILL.md 코어 디스패처에 의해 로드됩니다.

사용자가 선택한 완성도 수준에 따라:

## 🔴 낮음 (린) — 4단계

```
S1. JTBD 선언문 → references/02b-jtbd.md 로드
S2. HMW 1개 → references/03-define.md → 2.3 로드
S3. PR-FAQ → references/04a-prfaq.md 로드
S4. North Star → references/05a-northstar-aha.md 로드
(사용자가 모든 단계를 다른 프레임워크로 교체 가능)
────
최종 산출물 → 제품 스펙 요약 (미실행 필드는 "미실행"으로 표시)
```

## 🟡 중간 (표준) — 10단계

```
S1.  Persona 테이블 + Persona 카드 → references/02a-persona.md 로드
S2.  JTBD 분석 → references/02b-jtbd.md 로드
S3.  페인포인트 요약 테이블 → references/03-define.md 로드
S4.  HMW 질문 재구성 → references/03-define.md 로드
S5.  April Dunford 포지셔닝 → references/03-define.md 로드
S6.  PR-FAQ → references/04a-prfaq.md 로드
S7.  병렬 솔루션 + MVP + Not Doing List → references/04b-solutions.md + references/04c-mvp.md 로드
S8.  North Star + 3계층 시그널 + Aha Moment → references/05a-northstar-aha.md 로드
S9.  PMF 수준 평가 → references/05b-pmf-gtm.md 로드
S10. 제품 스펙 요약 → references/05c-validation-spec.md 로드
```

## 🟢 높음 (종합) — 16단계

```
S1.  Strategy Blocks + Rumelt → references/01-strategy.md 로드
S2.  Persona 테이블 + Persona 카드 → references/02a-persona.md 로드
S3.  JTBD 분석 → references/02b-jtbd.md 로드
S4.  OST Opportunity Solution Tree → references/02c-ost-journey.md 로드
S5.  User Journey Map → references/02c-ost-journey.md 로드
S6.  페인포인트 요약 테이블 → references/03-define.md 로드
S7.  HMW + April Dunford 포지셔닝 → references/03-define.md 로드
S8.  기회 평가 테이블 → references/03-define.md 로드
S9.  PR-FAQ → references/04a-prfaq.md 로드
S10. 병렬 프로토타입 → references/04b-solutions.md 로드
S11. Pre-mortem → references/04b-solutions.md 로드
S12. GEM + RICE → references/04b-solutions.md 로드
S13. MVP + Not Doing List → references/04c-mvp.md 로드
S14. North Star + 3계층 시그널 + Aha Moment → references/05a-northstar-aha.md 로드
S15. 가설 검증 계획 → references/05c-validation-spec.md 로드
S16. 제품 스펙 요약 → references/05c-validation-spec.md 로드
```

## 레퍼런스 로딩 규칙

각 단계에 진입할 때만 해당 레퍼런스 파일을 로드하세요 (모든 파일을 사전 로드하지 마세요). 위의 각 단계에 레퍼런스 경로가 주석으로 표시되어 있습니다.

## 최종 산출물 형식

**제품 스펙 요약** (완료된 단계만 통합; 미실행 필드는 "미실행"으로 표시)

완료 시, `references/rules-end-of-flow.md`에 따라 플로우 종료 규칙을 실행하세요.
