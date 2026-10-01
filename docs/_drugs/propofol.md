---
layout: default
title: Propofol
parent: 高證據等級 (L1-L2)
nav_order: 724
evidence_level: L2
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Propofol：從麻醉鎮靜到偏頭痛

## 一句話總結

Propofol（丙泊酚）是靜脈注射的全身麻醉與鎮靜藥。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **5 個相關臨床試驗登記**（其中 3 個直接以 propofol 治療偏頭痛）和 **20 篇文獻**支持這個方向，包含數項 RCT 與系統性回顧。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前沒有資料。依一般藥理知識，propofol 是 GABA-A 受體的正向異位調節劑，具鎮靜與麻醉作用。

偏頭痛被認為與皮質過度興奮及三叉神經血管系統活化有關。GABA 系統的抑制作用可能抑制這些過程。前臨床研究顯示，propofol 衍生物（propofol hemisuccinate）能抑制皮質擴散性抑制 (cortical spreading depression)，這是偏頭痛先兆的神經基礎（PMID 22390898）。

不過 propofol 對頭痛的作用機轉尚未完全確立。使用時需要在有監測的環境（如急診）進行，因為有鎮靜與呼吸抑制風險。

## 臨床試驗證據

以下依與主題的相關性排序。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | 完成 | 74 | 低劑量 propofol 用於兒童偏頭痛急診中止治療，為本組最強的試驗證據（相關性 A） |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | 完成 | 40 | 低劑量 propofol 輸注用於兒童偏頭痛，評估療效、安全劑量與作用持續時間（相關性 B） |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | 提前終止 | 12 | 低劑量 propofol 用於急診嚴重難治性偏頭痛；因提前終止，可用的療效資料有限（相關性 B） |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | 未知 | 130 | 比較 sevoflurane 與 propofol 維持麻醉後的術後頭痛發生率，屬麻醉問題，非偏頭痛治療（相關性 C） |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | NA | 完成 | 315 | 電針用於非體外循環冠狀動脈繞道手術的鎮痛，propofol 並非受試介入，相關性低（相關性 C） |

## 文獻證據

優先列出 RCT，其次為系統性回顧、指引與綜述。多數摘要只交代研究目的、未附結果，因此「主要發現」欄僅描述研究問題。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | 前瞻性隨機對照試驗，評估亞麻醉劑量 propofol 用於兒童偏頭痛的療效、副作用與住院時間 |
| [33070469](https://pubmed.ncbi.nlm.nih.gov/33070469/) | 2021 | RCT | Emerg Med Australas | 雙盲 RCT，比較 propofol 與安慰劑對成人急診偏頭痛 1 小時內頭痛緩解的效果 |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT（先導） | Emerg Med Australas | 先導 RCT，比較程序鎮靜劑量 propofol 與標準治療對急診偏頭痛的初始處置 |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | 比較 sumatriptan 加 propofol 與單用 sumatriptan 對急性偏頭痛的效果 |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | 雙盲 RCT，比較 propofol 合併 granisetron 與合併 metoclopramide 的症狀控制 |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | 系統性回顧 | Acad Emerg Med | 回顧 propofol 用於急診急性偏頭痛的安全性與療效，認為現有證據有限，可作為急診患者的選項之一 |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | 系統性回顧 | Headache | 網絡分析，比較各類注射藥物降低嚴重急性偏頭痛復發的效果 |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | 指引 | Headache | 美國頭痛學會 2025 年更新的成人急診偏頭痛注射藥物治療指引證據評估 |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | 綜述 | Expert Rev Neurother | 說明 propofol 用於超難治性偏頭痛的完整藥物概況，指出亞麻醉劑量曾被報告有益 |
| [23872997](https://pubmed.ncbi.nlm.nih.gov/23872997/) | 2013 | 簡短證據回顧 (BET) | Emerg Med J | 三項直接相關研究的結論認為，propofol 可能是安全有效的急診偏頭痛選項 |

## 香港上市資訊

資料中沒有劑型與核准適應症文字，以下僅列出品名與持證商。

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-27322 | DIPRIVAN INJ 1% | Aspen Pharmacare Asia Limited |
| HK-66287 | PROPOFOL-LIPURO EMULSION FOR INJECTION/INFUSION 500MG/50ML | B. Braun Medical (HK) Ltd |
| HK-55671 | FRESOFOL INJ 1% MCT/LCT | Fresenius Kabi Hong Kong Limited |
| HK-66286 | PROPOFOL-LIPURO EMULSION FOR INJECTION/INFUSION 200MG/20ML | B. Braun Medical (HK) Ltd |
| HK-49677 | PROPOFOL-LIPURO INJ 1% | B. Braun Medical (HK) Ltd |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 2/3 試驗（NCT01604785），另有多項成人與兒童的急診偏頭痛 RCT 和系統性回顧，證據等級為 L2。但這些研究多為小型、單中心，作用機轉也未完全確立。
- propofol 有鎮靜與呼吸抑制風險，只適合在有監測的急診或醫療環境使用，不宜擴大到一般門診或居家情境。

**其他預測適應症：**
- 先兆型偏頭痛中的腦幹先兆型（L4，Research Question）：只有間接證據，無針對此亞型的研究。
- Prinzmetal 心絞痛（L4，Hold）：僅有麻醉中誘發冠狀動脈痙攣的個案報告，屬安全性警訊而非療效，需留意。
- 腎因性抗利尿激素不適當分泌症候群（L5，Hold）：只有模型預測，沒有任何研究。
- Tourette 症候群（L4，Hold）：只有深部腦刺激手術中的鎮靜使用，並非治療 tic。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料（目前缺口 DG001，屬阻擋項，必須先補齊才能進入安全性篩選）
- 補充 DrugBank 的作用機轉資料（缺口 DG002）
- 取得確認各 RCT 的主要終點結果（頭痛緩解率、復發率），以評估療效大小
- 訂定急診使用的劑量、監測設備與人員資格規範（含呼吸抑制處置）
- 確認香港各許可證的核准適應症與劑型，並評估超適應症使用的合規性

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

