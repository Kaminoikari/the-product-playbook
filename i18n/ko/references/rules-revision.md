# 🔄 리비전 모드 단계 시퀀스 (12단계 + 최종 산출물)

> 이 파일은 리비전 모드의 권위 있는 단계 정의입니다. SKILL.md 코어 디스패처에 의해 로드됩니다.

## 단계 시퀀스

```
Phase 0: 현상 분석
  S1.  기존 제품 리뷰 (사용자 데이터 개요 + 핵심 지표 + 알려진 이슈 + 보안 상태)
  S2.  기존 사용자 JTBD 재검토 (어떤 Job이 잘 되고 있는가? 어떤 것이 안 되는가?)

Phase 1: 문제 수렴
  S3.  사용자 페인포인트 수집 (리텐션/이탈 분석 + 사용자 피드백 종합 + 행동 데이터)
  S4.  페인포인트 요약 테이블 → references/03-define.md → 2.1 로드
  S5.  포지셔닝 재평가 → references/03-define.md → 2.2 로드 (초점: 포지셔닝 조정이 필요한가?)
  S6.  HMW 질문 재구성 → references/03-define.md → 2.3 로드
  S7.  기회 평가 테이블 → references/03-define.md → 2.4 로드

Phase 2: 솔루션 설계
  S8.  PR-FAQ → references/04a-prfaq.md 로드 (리비전 후 경험 묘사)
  S9.  Pre-mortem → references/04b-solutions.md → 3.3 로드
  S10. MVP 범위 + Not Doing List → references/04c-mvp.md 로드 (초점: 변경할 것 / 변경하지 않을 것)

Phase 3: 검증
  S11. North Star + Aha Moment → references/05a-northstar-aha.md 로드 (리비전 전후 지표 비교)
  S12. 가설 검증 계획 → references/05c-validation-spec.md 로드
────
최종 산출물 → 제품 스펙 요약 (리비전 에디션)
```

### S1 사전 단계: 제품 컨텍스트 로딩

S1에 진입하기 전, `references/rules-context.md`를 로드하고 `.product-context.md`를 확인하세요:

- **완전한 컨텍스트 사용 가능 (시나리오 1)**: PMF 수준, North Star, 알려진 페인포인트, 보안 상태, 가장 최근 3개 Decision History 항목을 자동 입력. S1 안내를 **델타 모드**로 전환: "지난 평가에서 PMF 수준은 [X], North Star 지표는 [Y]였습니다. 변경된 것이 있나요? 최신 DAU/MAU와 리텐션 수치는?" — 이전에 수집된 의사결정 이력과 알려진 페인포인트는 재수집 불필요.
- **컨텍스트 사용 불가 (시나리오 2)**: Context Bootstrap 트리거 (`rules-context.md` 섹션 4, 라운드 1 + 3), 그 다음 아래 표준 S1 데이터 수집 진행.
- **부분 컨텍스트 (시나리오 3)**: Decision History에서 기능 변경 이력 가져오기 (어떤 모듈이 변경되었고 어떤 리스크가 식별되었는지 파악), 하지만 전체 제품 전략과 지표는 질문 (이전 작업은 기능 확장만 다뤘고 전체적 관점이 부족함).

### S1 표준 안내

> 리비전 모드의 S1은 사용자에게 기존 제품 데이터를 제공하도록 능동적으로 질문합니다: DAU/MAU, 리텐션율, 주요 사용자 피드백, 이전 버전 결정 등. 컨텍스트가 일부 답변을 이미 입력한 경우 재수집이 아닌 확인.
> S1은 또한 현재 보안 상태를 수집합니다: 기존 인증/인가 메커니즘, 알려진 보안 취약점 또는 기술 부채, 최근 보안 인시던트. 이 정보는 리비전의 리스크 평가와 Pre-mortem에 영향을 미칩니다.

### 빠른 경로

사용자가 S1에서 충분한 데이터를 제공할 때 (사용자 피드백, 지표, 페인포인트 포함), S4-S7 (페인포인트 → 포지셔닝 → HMW → 기회 평가)을 단일 대화 턴에서 작성할 수 있으며, 4번이 아닌 1번의 확인만 필요합니다. 트리거 조건: S3에서 수집된 페인포인트 목록이 이미 명확한 우선순위와 데이터 지원을 가지고 있는 경우. 하드 게이트 규칙은 변경되지 않음 — 각 단계의 산출물은 여전히 완전히 제시되어야 하며; 확인 리듬만 가속됩니다.

## 레퍼런스 로딩 지침

| 단계 | 레퍼런스 파일 |
|------|-------------|
| S1-S3 | 외부 레퍼런스 필요 없음 (사용자에게 직접 데이터 제공 안내) |
| S4-S7 | `references/03-define.md` |
| S8 | `references/04a-prfaq.md` |
| S9 | `references/04b-solutions.md` |
| S10 | `references/04c-mvp.md` |
| S11 | `references/05a-northstar-aha.md` |
| S12 + 최종 산출물 | `references/05c-validation-spec.md` |

## 최종 산출물 형식

**리비전 제품 스펙 요약**: 전후 비교 + 변경할 것 / 변경하지 않을 것 + 성공 지표

완료 시, `references/rules-end-of-flow.md`에 따라 플로우 종료 규칙을 실행하세요.
