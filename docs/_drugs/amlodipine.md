---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amlodipine：預測新適應症為腦幹梗塞 (Brain stem infarction)（證據等級 L5）。原適應症：高血壓、中風、腦血管疾病、腦梗塞、Prinzmetal 心絞痛"
---

# Amlodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Amlodipine：從高血壓與腦血管疾病到腦出血（Intracerebral Hemorrhage）

## 一句話總結

Amlodipine 是鈣離子通道阻斷劑，原本用於高血壓、中風相關疾病、腦血管疾病、腦梗塞及變異型心絞痛（Prinzmetal angina）。
TxGNN 模型預測的第一名是**腦幹梗塞 (brain stem infarction)**，但該項僅有模型預測、沒有任何研究支持。
證據最完整的是第 10 名**腦出血 (Intracerebral Hemorrhage)**：有 **4 個臨床試驗**（含 1 個已完成的 Phase 3 試驗）和 **9 篇文獻**，但證據來自三合一複方策略，無法單獨歸因於 amlodipine。

> 說明：依規則，快速總覽以預測排名第 1 的適應症為準；下文另以證據最充分的腦出血作補充評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、中風、腦血管疾病、腦梗塞、Prinzmetal 心絞痛（許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症（排名第 1） | 腦幹梗塞 (Brain stem infarction) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |
| 補充：證據最強的預測 | 腦出血（分數 99.79%，證據等級 L2，Proceed with Guardrails） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Amlodipine 屬於鈣離子通道阻斷劑（一般已知為二氫吡啶類），透過阻斷血管平滑肌的 L 型鈣離子通道，使小動脈擴張、降低血壓。

腦幹梗塞屬於腦梗塞的一種，而 amlodipine 本來就已被列為腦血管疾病與中風相關適應症。因此模型的高分，較可能反映的是既有的腦血管適應症（藉由降壓與血管擴張），而不是新的獨立療效。目前沒有針對腦幹梗塞的臨床試驗或文獻。

在其他預測中，腦出血的理由最為充分：強化血壓控制是預防腦出血復發的關鍵可調整因素，而 amlodipine 是 TRIDENT 試驗三合一低劑量單一藥丸（搭配 ARB 與利尿劑）的核心成分。

---

## 臨床試驗證據

以下為排名第 1 的腦幹梗塞：**目前無相關臨床試驗登記**。

為供決策參考，以下列出證據最強的預測「腦出血」之臨床試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | 已完成 | 1671 | TRIDENT：三合一低劑量降壓藥丸（含 amlodipine）用於預防腦出血後再中風，為組合療法證據 |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | 招募中 | 140 | 腦出血後以三種降壓藥控制血壓（TRICH 分數），規模小、屬早期 |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | 提前終止 | 4 | TRIDENT MRI 子研究，僅 4 人，無可用資料 |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | 提前終止 | 1 | TRIDENT 認知子研究，僅 1 人，無可用資料 |

---

## 文獻證據

排名第 1 的腦幹梗塞：**目前無相關文獻**。

腦出血的主要文獻如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT（TRIDENT 主要報告） | N Engl J Med | 探討腦出血後加用三合一低劑量降壓藥丸，能否進一步降壓並降低中風復發風險；結果須自原文確認 |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | 試驗設計論文 | Int J Stroke | TRIDENT 的設計與進度；單一藥丸組合為腦出血二級預防策略 |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT 設計（間接） | Hypertens Res | CASE-J 試驗設計，以 candesartan 為主，與 amlodipine 關聯間接 |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | 鈣離子拮抗劑在高血壓的用途與療效比較 |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | 病例報告 | Ann Pharmacother | 丘腦出血性中風患者疑似 amlodipine 引起血管性水腫 |

---

## 香港上市資訊

香港共有 20 張有效的單方許可證，皆為單方製劑，無已取消者。許可證資料中未載明劑型與核准適應症文字。以下列出 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55770 | PMS-AMLODIPINE TAB 5MG | 未載明 | 未載明 |
| HK-65871 | AMLOCOR TABLETS 10MG | 未載明 | 未載明 |
| HK-56593 | AMLODIPINA FARMOZ TAB 5MG | 未載明 | 未載明 |
| HK-66898 | KARDAM 10 TABLETS 10MG | 未載明 | 未載明 |
| HK-63420 | AMDIVASC TABLETS 5MG | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容，僅供參考）：肝衰竭／肝病、腎臟疾病、胰臟炎、膽囊疾病、甲狀腺功能低下、血管性水腫（含遺傳性）、全身性紅斑性狼瘡、肌病變、糖尿病／糖尿病酮酸中毒、嗜中性白血球低下、低血壓、副甲狀腺功能亢進等。
- **藥物交互作用**：共查得 100 筆，以下為部分中度（Moderate）交互作用：糖皮質類固醇（hydrocortisone、betamethasone、budesonide、dexamethasone）、aprepitant、乙醯水楊酸（aspirin）、bupropion、各類鈣劑、canagliflozin、dapagliflozin、clarithromycin、clotrimazole。
- **預測適應症相關的特別提醒**：鈣離子通道阻斷劑可能削弱缺氧性肺血管收縮，不建議用於肺疾病所致的肺高壓；腦出血情境須避免低血壓。

仿單的警語與禁忌症資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（排名第 1 的腦幹梗塞）；若聚焦腦出血，則為 **Proceed with Guardrails**。

**理由：**
- 腦幹梗塞僅有模型預測（L5），沒有試驗或文獻，且很可能只是反映既有的腦梗塞適應症。
- 腦出血有已完成的 Phase 3 TRIDENT 試驗（n=1671）及 2026 年發表的報告，但測試的是含 amlodipine 的三合一組合策略，無法確認 amlodipine 單獨的貢獻，因此建議以降壓策略的一部分來看待，並附帶防護條件。

**若要推進需要：**
- 從 TRIDENT 原始論文（PMID 42019018）直接核實主要結果與安全性數據
- 補充 amlodipine 的作用機轉資料
- 取得香港仿單的警語與禁忌症
- 制定腦出血後使用的監測計畫（避免低血壓、血壓目標與追蹤）
- 其他預測（如肺高壓類）因證據薄弱或有機轉上的風險，不建議推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

