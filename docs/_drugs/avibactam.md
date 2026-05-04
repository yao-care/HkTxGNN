---
layout: default
title: Avibactam
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Avibactam
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

# Avibactam：從耐藥菌複方抗菌治療到多適應症老藥新用評估

## 一句話總結

Avibactam 是新型非共價鍵結合 β-內醯胺酶抑制劑，臨床上以複方製劑（如 Ceftazidime-avibactam）形式用於對抗耐藥性革蘭陰性菌感染，香港目前尚未上市、無許可證記錄。
TxGNN 模型對 Avibactam 預測了 10 個新適應症，最高分為**鏈球菌性肺炎（Streptococcal Pneumonia，99.70%）**，最具間接機轉支持的為**金黃色葡萄球菌感染（S. aureus Infection，98.97%）**，後者有 **2 個臨床試驗**及 **20 篇文獻**（相關性有限）。
機轉分析顯示絕大多數預測為知識圖譜假陽性，整體建議 **Hold**，所有候選均暫不具備推進條件。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（香港未上市，無許可證記錄） |
| 最高分預測適應症 | 鏈球菌性肺炎（Streptococcal Pneumonia） |
| TxGNN 預測分數（最高） | 99.70% |
| 最佳證據等級 | L4（金黃色葡萄球菌感染，排名第 7） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 10 適應症預測總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 機轉相符性 | 建議 |
|------|--------|-----------|---------|-----------|------|
| 1 | 鏈球菌性肺炎（Streptococcal Pneumonia） | 99.70% | L5 | ❌ 不符（PBP 變異主導耐藥，非 β-內醯胺酶） | Hold |
| 2 | 嚴重流感易感性（Influenza, severe） | 99.28% | L5 | ❌ 不符（RNA 病毒，無抗病毒機轉） | Hold |
| 3 | 輸尿管結核（Ureter Tuberculosis） | 99.11% | L5 | ❌ 不符（MTB 固有耐藥，CZA 臨床資料極稀缺） | Hold |
| 4 | 泌尿道血吸蟲病（Urinary Schistosomiasis） | 99.06% | L5 | ❌ 不符（真核寄生蟲，無抗寄生蟲靶點） | Hold |
| 5 | 多株性高黏滯症（Polyclonal Hyperviscosity） | 99.01% | L5 | ❌ 不符（免疫球蛋白疾病，無免疫調節機轉） | Hold |
| 6 | 高澱粉酶血症（Hyperamylasemia） | 99.01% | L5 | ⚠️ 反向關聯（可能為副作用，非治療適應症） | Hold |
| 7 | 金黃色葡萄球菌感染（S. aureus Infection） | 98.97% | L4 | ⚠️ 間接機轉假說（Ceftaroline 組合保護） | Research Question |
| 8 | 腎結核（Renal Tuberculosis） | 98.93% | L5 | ❌ 不符（MTB，標準 RIPE 方案，無 avibactam 臨床依據） | Hold |
| 9 | 肺鱗狀細胞癌（Squamous Cell Lung Carcinoma） | 98.86% | L5 | ❌ 不符（腫瘤，無抗增殖/促凋亡機轉） | Hold |
| 10 | 先天性無白蛋白血症（Congenital Analbuminemia） | 98.84% | L5 | ❌ 不符（ALB 基因缺陷，無蛋白合成修正機轉） | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Avibactam 是一種非共價鍵結合型 β-內醯胺酶抑制劑，以複方製劑形式（如 Ceftazidime-avibactam）用於耐藥性革蘭陰性菌感染治療，核心機轉為可逆性共價抑制 Ambler Class A（KPC、ESBLs）、Class C（AmpC）及部分 Class D（OXA-48）型 β-內醯胺酶，保護配對的 β-內醯胺類抗生素恢復對耐藥菌的抗菌活性。

TxGNN 預測的 10 個適應症，機轉分析揭示了明顯的**系統性假陽性問題**：鏈球菌性肺炎的耐藥機轉為青黴素結合蛋白（PBP）突變，與 β-內醯胺酶無關；流感為 RNA 病毒感染；血吸蟲病為真核寄生蟲感染；肺癌為腫瘤疾病——這些均與 Avibactam 的純抗菌機轉完全脫節，高預測分數很可能來自知識圖譜中「肺炎節點」「感染節點」「泌尿系統節點」的圖譜相鄰性偽關聯。特別值得注意的是**高澱粉酶血症（排名第 6）**：TxGNN 可能捕捉到的是 Avibactam 導致胰腺毒性（即藥物→副作用）的方向，而非治療關係，這是知識圖譜方向性編碼的系統性盲點。

唯一具備間接機轉假說的是**金黃色葡萄球菌感染（排名第 7）**：當 Avibactam 與具抗 MRSA 活性的 Ceftaroline 組合使用時，Avibactam 理論上可抑制 β-內醯胺酶、保護 Ceftaroline 免受水解，間接提升抗 MRSA 覆蓋能力。體外研究（PMID 22733066）及多菌感染動物模型（PMID 24041891）提供了初步前臨床支持。然而，S. aureus 的主要耐藥機制為 PC1 型 Class A penicillinase，Avibactam 對其的抑制效力存疑，且目前缺乏針對此適應症的 Phase 2/3 臨床試驗佐證。

---

## 臨床試驗證據

> 以下試驗來自排名第 7（金黃色葡萄球菌感染）適應症；排名第 1–6 及第 8–10 的適應症均無相關臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03941951](https://clinicaltrials.gov/study/NCT03941951) | N/A | 未知 | 900 | 安達盧西亞公共衛生系統 14 家醫院新型抗生素（含 Ceftazidime-avibactam）優化使用之準實驗性多中心前後研究，非 S. aureus 感染的治療性試驗，直接相關性低（Grade C） |
| [NCT06634940](https://clinicaltrials.gov/study/NCT06634940) | N/A | 招募中 | 1000 | 肝硬化相關感染抗菌素耐藥性國際監測研究，屬流行病學觀察設計，不直接評估 Avibactam 療效，直接相關性低（Grade C） |

---

## 文獻證據

> 以下文獻來自排名第 7（金黃色葡萄球菌感染）適應症的 20 篇回傳結果，優先列出最具直接相關性的 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22733066](https://pubmed.ncbi.nlm.nih.gov/22733066/) | 2012 | In vitro | Antimicrob Agents Chemother | Ceftaroline-avibactam 對多種 β-內醯胺酶產生菌及不同 SCCmec 型 MRSA/MSSA 的體外活性，Avibactam 顯著擴展廣譜抗菌覆蓋 |
| [24041891](https://pubmed.ncbi.nlm.nih.gov/24041891/) | 2013 | 動物實驗 | Antimicrob Agents Chemother | 多菌感染小鼠模型：模擬人體劑量 Ceftaroline fosamil-avibactam（600mg/600mg q8h）對 MRSA、MSSA 及革蘭陰性菌（E. coli、Enterobacter）混合感染具有效療效 |
| [40910659](https://pubmed.ncbi.nlm.nih.gov/40910659/) | 2025 | Review | Curr Opin Crit Care | MDR/XDR 重症感染（血流感染及 VAP）管理建議最新綜述，涵蓋 Avibactam 組合藥在 RCT 中的現有證據與臨床推薦脈絡 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | 新型抗生素仿單外使用 vs 正式適應症建議之比較評估，涵蓋 Avibactam 組合藥對 MDR Gram-positive（含 MRSA）之標籤外用途討論 |
| [25667169](https://pubmed.ncbi.nlm.nih.gov/25667169/) | 2015 | Review | Langenbeck's Arch Surg | ESKAPE 病原體新型抗菌藥物開發回顧，Ceftazidime-avibactam 列為重要新藥，奠定廣譜抗菌的科學依據 |
| [29507064](https://pubmed.ncbi.nlm.nih.gov/29507064/) | 2018 | Retrospective Cohort | Antimicrob Agents Chemother | 77 例 CRE 感染 Ceftazidime-avibactam 治療分析：30 天存活率 81%、90 天 69%，肺炎及腎臟替代療法為治療失敗獨立危險因子 |
| [28314920](https://pubmed.ncbi.nlm.nih.gov/28314920/) | 2017 | Review | Med Klin Intensivmed | 六種新型抗生素（含 Ceftazidime-avibactam）臨床應用概述，部分因研究結果尚不充分僅提供專家意見 |
| [40426531](https://pubmed.ncbi.nlm.nih.gov/40426531/) | 2025 | Retrospective Cohort | Antibiotics | 義大利 Palermo 大學醫院 2018–2024 年耐藥菌血流感染流行病學及預後 7 年回顧，提供耐藥菌感染背景數據 |
| [36143934](https://pubmed.ncbi.nlm.nih.gov/36143934/) | 2022 | Observational | Medicina | 醫院環境抗生素濫用與 AMR 觀察研究，分析包含 S. aureus 在內五種耐藥菌的分佈及敏感性變化趨勢 |
| [40989184](https://pubmed.ncbi.nlm.nih.gov/40989184/) | 2025 | Review | Front Cell Infect Microbiol | 天津 14 家醫院 2021–2023 年臨床分離株 AMR 趨勢分析，含 S. aureus 耐藥模式，用於指導精準抗菌管理策略 |

---

## 香港上市資訊

Avibactam 目前在香港**無已核准許可證記錄**（總計 0 張），尚未在香港正式上市。如需臨床使用 Avibactam 相關組合製劑（如 Ceftazidime-avibactam），需向衞生署藥物辦公室申請特別進口許可。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 文獻補充提示：（1）Ceftazidime-avibactam 在部分病例中有胰腺毒性（澱粉酶升高）不良反應報告，此正是 TxGNN 預測「高澱粉酶血症」的可能原因；（2）腎臟替代療法患者的治療失敗風險較高（Shields et al., 2018），使用時應評估劑量調整。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測的 10 個適應症中，9 個因機轉根本不相容而無推進依據（L5，0 支持證據）；唯一具間接機轉假說的金黃色葡萄球菌感染（L4）目前僅有前臨床（體外及動物）數據，缺乏 Phase 2/3 臨床試驗驗證，加之 Avibactam 在香港未上市，缺乏本地監管基礎，整體暫不具備推進條件。

**若要推進（金黃色葡萄球菌感染方向）需要：**
- 補充完整作用機轉資料（DrugBank MOA 查詢，解除 DG002 資料缺口）
- 取得衞生署相關仿單以評估安全性警語及禁忌症（解除 DG001 Blocking 缺口）
- 針對 Ceftaroline-avibactam 組合治療 MRSA 感染進行系統性文獻回顧，確認是否存在 Phase 2/3 臨床試驗數據
- 評估在香港引進 Avibactam 組合製劑的監管可行性（特別用藥申請途徑）
- 優化 TxGNN 知識圖譜的方向性編碼，明確區分「副作用邊」與「治療邊」，以降低本案所見的系統性假陽性率
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

