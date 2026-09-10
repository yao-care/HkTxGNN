---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 565
evidence_level: L5
indication_count: 5
---

# Pegaspargase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# PEGASPARGASE：原適應症資料缺口，TxGNN 指向 Precursor Lymphoblastic Leukemia/Lymphoma（急性淋巴母細胞性白血病／淋巴瘤）

## 一句話總結

PEGASPARGASE（DrugBank DB00059）目前在此證據包中缺乏完整的原適應症與作用機轉紀錄，香港亦**尚未上市**。
TxGNN 模型將其最高分預測指向**Precursor Lymphoblastic Leukemia/Lymphoma（前驅淋巴母細胞白血病／淋巴瘤，即 ALL 相關族群）**，
評分達 **99.96%**，且已有 **50 個相關臨床試驗**（含多個完成之 Phase 3 RCT）與 **20 篇文獻**支持——這其實反映該藥在國際上已是 ALL 治療的既有標準用藥，而非全新假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 證據包未記錄（資料缺口） |
| 預測新適應症 | Precursor Lymphoblastic Leukemia/Lymphoma（前驅淋巴母細胞白血病／淋巴瘤） |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1（≥2 個已完成 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料，證據包中也未記錄原始核准適應症。不過，從附帶的臨床試驗與文獻可以清楚看到，PEGASPARGASE 是急性淋巴母細胞白血病／淋巴瘤（ALL/LBL）多重化療方案中的關鍵成分：其作用原理是耗竭血漿中的天門冬醯胺（asparagine），使依賴外源天門冬醯胺維生的淋巴母細胞因蛋白質合成受阻而死亡（文獻 PMID 17696798、30823860 有描述此機轉）。

值得注意的是，這裡 TxGNN 預測分數最高的疾病「Precursor Lymphoblastic Leukemia/Lymphoma」與大量已完成 Phase 3 RCT（如 NCT00671034、NCT00819351、NCT00549848、NCT00187083）高度重疊，顯示模型很可能正確捕捉到藥物與疾病之間**已經確立**的關聯，而非發現全新的老藥新用機會。這類「已知關聯被模型重新識別」的結果，本身是驗證模型可信度的正向訊號，但對於「新適應症拓展」的商業與研究價值有限。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | 完成 | 166 | Calaspargase pegol 對比 pegaspargase 併用化療治療高風險 ALL 的隨機對照試驗 |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | 完成 | 650 | NOPHO 方案：間歇式 vs. 連續式 PEG-asparaginase 給藥比較，評估無事件存活率 |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | 完成 | 600 | Total Therapy XVI：高劑量 vs. 常規劑量 PEG-asparaginase 之藥動/藥效比較 |
| [NCT00187083](https://clinicaltrials.gov/study/NCT00187083) | Phase 3 | 完成 | 40 | 天然 asparaginase（E. coli/Erwinia）vs. PEG-asparaginase 於復發/難治兒童 ALL 誘導治療之比較 |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | 完成 | 6136 | 國際兒童青少年 ALL 合作治療協定，比較多種合併化療方案（含 PEG-asparaginase） |
| [NCT01540812](https://clinicaltrials.gov/study/NCT01540812) | N/A | 完成 | 418 | 成人高風險 BCR/ABL 陰性 ALL：誘導與鞏固治療加入 PEG-ASP 之方案優化 |
| [NCT02393859](https://clinicaltrials.gov/study/NCT02393859) | Phase 3 | 完成 | 111 | Blinatumomab 鞏固治療 vs. 傳統含 asparaginase 化療於高風險首次復發 B-ALL 兒童 |
| [NCT03267030](https://clinicaltrials.gov/study/NCT03267030) | Phase 2 | 完成 | 55 | Eryaspase 用於對 PEG-asparaginase 過敏、Ph(-) ALL 患者之藥動/安全性研究 |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | 進行中 | 9350 | 標準風險 B-ALL/局限性 B-LLy 之風險調整化療方案大型試驗 |
| [NCT04843150](https://clinicaltrials.gov/study/NCT04843150) | N/A | 完成 | 320 | ALLTogether 前導研究：PEG-asparaginase 首劑之藥動學與免疫原性評估 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231 Phase III 試驗：bortezomib 加入新診斷 T-ALL/T-LL 治療並嘗試減少預防性顱腦放療 |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232：地塞米松與高劑量甲氨蝶呤改善高風險 B-ALL 兒童及年輕成人存活率 |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434 Phase III：nelarabine 用於新診斷 T-ALL 之隨機對照試驗 |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | RCT | J Clin Oncol | DFCI 11-001：calaspargase pegol 與 pegaspargase 於兒童 ALL 之療效與毒性比較 |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | 臨床試驗 | Blood Advances | GIMEMA LAL1913：pegaspargase 加入成人 Ph- ALL/LL 風險導向化療方案之結果 |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | 臨床試驗（Phase 2） | Leukemia | Venetoclax 加入 hyper-CVAD+nelarabine+PEG-asparaginase 治療 T-ALL/LBL 之長期追蹤 |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | 臨床試驗（Phase 2） | Int J Hematol | 日本多中心研究：pegaspargase 於初治 ALL 患者之療效、安全性與藥動學 |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review | Blood | 成人 ALL 患者使用 pegasparaginase 之毒性處置經驗（How I treat） |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Pegaspargase 於急性淋巴母細胞白血病治療之藥物綜述 |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | PEG-asparaginase 作用機轉、療效與過敏反應限制之綜述 |

## 細胞毒性

**判定依據：** 證據包未提供 DrugBank categories，但預測適應症（前驅淋巴母細胞白血病/淋巴瘤）與大量臨床試驗均將本藥列為多重化療方案之一員，文獻（PMID 17696798、31977001）明確描述其透過耗竭天門冬醯胺產生細胞毒殺效果，屬抗腫瘤藥物範疇。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（酵素類抗腫瘤劑，機轉為胺基酸耗竭而非直接 DNA 損傷） |
| 骨髓抑制風險 | 低（PMID 31977001 指出其毒性特徵與其他化療藥物不同，非典型骨髓抑制；常見毒性為肝毒性、胰臟炎、高三酸甘油酯血症、過敏反應與血栓） |
| 致吐性分級 | 證據包文獻未特別描述致吐性，建議參考原廠仿單 |
| 監測項目 | 肝功能（ALT/AST）、胰臟酵素（脂肪酶/澱粉酶）、三酸甘油酯、凝血功能（纖維蛋白原、抗凝血酶）、血糖、過敏反應徵象 |
| 處置防護 | 屬抗腫瘤藥物，需依細胞毒性藥物處置規範操作（防護裝備、溢出處理等） |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TFDA/香港仿單警語與禁忌症資料為 Blocking 等級缺口（DG001），依規定無法進入 S1 安全性初評。
- 本藥於香港**尚未上市**（0 張許可證），即使療效證據等級達 L1，仍缺乏在地法規與安全性基礎。
- 此外，TxGNN 預測的最高分適應症與該藥國際上已知的既有用途高度重疊，屬模型驗證性結果而非全新老藥新用假說，優先度應低於真正新穎的候選適應症（如清單中 rank 2-4 的 CLL/SLL、濾泡性淋巴瘤，惟該三項目前為 L5，僅有模型分數、無任何試驗或文獻支持，同樣建議 Hold）。

**若要推進需要：**
- 取得香港（或原廠）仿單之警語、禁忌症與 DDI 資料，補齊 S1 安全性初評
- 補充 DrugBank 之作用機轉（MOA）與藥物分類資料，以強化機轉關聯性分析
- 確認台灣/香港是否有引進此藥的上市計畫或恩慈使用管道
- 若要評估 rank 2-4（CLL/SLL、濾泡性淋巴瘤）等真正新穎適應症，需先進行文獻與試驗檢索以驗證機轉合理性，目前僅有模型端預測，證據等級為 L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

