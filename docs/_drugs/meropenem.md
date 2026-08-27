---
layout: default
title: Meropenem
parent: 中證據等級 (L3-L4)
nav_order: 403
evidence_level: L3
indication_count: 5
---

# Meropenem
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Meropenem：從細菌感染治療到細菌性關節炎 (Bacterial Arthritis)

## 一句話總結

Meropenem 是廣效型 Carbapenem 類抗生素，原用於治療嚴重全身性細菌感染。
TxGNN 模型預測它可能對**細菌性關節炎 (Bacterial Arthritis)** 有效，
目前有 **1 個臨床試驗**（藥物相關性較低）和 **20 篇文獻**支持這個方向，其中多篇聚焦骨關節感染致病菌之藥物敏感性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染症（廣效型 Carbapenem 類抗生素；香港未上市，無核准適應症文字可查） |
| 預測新適應症 | 細菌性關節炎 (Bacterial Arthritis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 詳細作用機轉資料（Data Gap）。但根據既有藥理學共識與本次證據收集所得之機轉論述，Meropenem 屬 Carbapenem 類 β-內醯胺抗生素，透過抑制細菌青黴素結合蛋白 (Penicillin-Binding Protein, PBP)，阻斷細胞壁合成而產生殺菌作用，對多數格蘭氏陽性菌、格蘭氏陰性菌及厭氧菌均具廣效殺菌活性。

Meropenem 原本用於治療嚴重全身性細菌感染（如院內肺炎、複雜性腹腔內感染、腦膜炎、菌血症等），與細菌性關節炎同屬需要高組織穿透力、快速殺菌之嚴重感染範疇，兩者在治療邏輯上具高度相似性。

證據包中的機轉關聯性分析指出：「Meropenem 為廣效 PBP 抑制劑，對造成化膿性/感染性關節炎之常見致病菌（Staphylococcus spp.、Streptococcus spp.、部分格蘭氏陰性菌）具殺菌活性，且已知可穿透關節滑液及骨關節組織，臨床上已作為嚴重或多重抗藥性骨關節感染的經驗性/搶救性治療選項」。換言之，這並非全新機轉假說，而是既有臨床實務（骨關節感染經驗性用藥）的知識圖譜再確認，機轉關聯性強。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | 已完成 | 624 | 研究急性白血病/幹細胞移植兒童病人使用 levofloxacin 預防菌血症之效果；研究藥物為 **levofloxacin 而非 meropenem**，且終點為感染預防而非細菌性關節炎治療，相關性等級 C，僅供高風險感染族群背景參考 |

**說明：** 目前無直接針對 meropenem 治療細菌性關節炎之臨床試驗登記，此為證據等級未達 L1/L2 的主因。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | 回溯性世代研究 | Indian Journal of Medical Microbiology | 22 例骨骼肌肉受侵犯之類鼻疽感染回顧，敗血性關節炎與骨髓炎病例分離株對 meropenem 均具敏感性 |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | 回溯性世代研究 | Le infezioni in medicina | 骨關節類鼻疽感染回溯性世代研究，描述此類罕見骨關節侵犯病人之臨床特徵 |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | 世代研究 | Clinical Laboratory | 分析 4 歲以下兒童骨關節感染 (BJI) 之病原菌分布與抗藥性 |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | 回溯性研究 | Eur J Orthop Surg Traumatol | 建立非脊椎骨科感染經驗性抗生素選擇之抗生素圖譜 (antibiogram) |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case Report | Pharmaceuticals (Basel) | 免疫功能正常成人罕見髖關節化膿性關節炎案例（Bacillus/Paenibacillus 感染） |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | 體外研究 | J Bone Joint Surg Am | 評估 meropenem 等替代抗生素於 PMMA 骨水泥中之熱穩定性與釋放藥動學，支持局部骨關節感染治療應用潛力 |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | 動物模型研究 | Int J Antimicrob Agents | 兔隻模型中以 colistin 骨水泥治療碳青黴烯酶陽性克雷伯氏菌人工關節感染，反映抗藥性骨關節感染治療之臨床挑戰 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | 探討多重抗藥性/廣泛抗藥性細菌感染之抗生素標籤外使用與正式治療建議，涵蓋 carbapenem 類藥物角色 |
| [2808217](https://pubmed.ncbi.nlm.nih.gov/2808217/) | 1989 | 體外藥理研究 | J Antimicrob Chemother | Meropenem 對臨床分離株（含 Pseudomonas）之體外抑菌/殺菌活性經典研究，確立廣效殺菌基礎 |
| [38134096](https://pubmed.ncbi.nlm.nih.gov/38134096/) | 2023 | Case Report | Medicine | 痛風性關節炎病人併發 Campylobacter fetus 引發腰肌膿瘍之案例報告 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本次評估中「TFDA/當地仿單警語與禁忌症」被標記為 **Blocking 等級資料缺口 (DG001)**，在補齊前無法進入 S1 安全性初評階段，藥物交互作用查詢也未取得結果（query_status: not_found）。

---

## 其他預測適應症（供未來評估參考）

除細菌性關節炎外，本次評估同時針對 Meropenem 產出以下候選適應症，證據強度差異較大，列於此供後續排序參考：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議決策 | 備註 |
|------|------|-----------|---------|---------|------|
| 2 | 會厭炎 (Epiglottitis) | 99.91% | L5 | Hold | 無任何臨床試驗或文獻直接佐證，僅為知識圖譜相似性預測 |
| 3 | 金黃色葡萄球菌感染 (Staphylococcus aureus infection) | 99.85% | L3 | Proceed with Guardrails | 對 MSSA 有明確活性，但對 MRSA 普遍無效，須以藥敏結果為前提 |
| 4 | 喉炎 (Laryngitis) | 99.59% | L4 | Hold | 現有文獻多屬深頸部感染/縱膈炎相關病例，非直接針對喉炎療效 |
| 5 | 副傷寒 (Paratyphoid fever) | 99.57% | L3 | Proceed with Guardrails | 屬 XDR 傷寒/副傷寒沙門氏菌之搶救性治療選項，缺乏前瞻性對照試驗 |

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對細菌性關節炎 Bacterial Arthritis）

**理由：**
- 多篇回溯性世代研究與病例報告顯示，meropenem 對造成骨關節感染之常見致病菌（含類鼻疽菌、多重抗藥性格蘭氏陰性菌）具殺菌活性且能穿透骨關節組織，臨床實務上已作為嚴重/抗藥性骨關節感染之經驗性或搶救性用藥，機轉關聯性強，非首次假說。
- 但唯一收錄之臨床試驗（NCT01371656）研究藥物為 levofloxacin 而非 meropenem，相關性偏低，目前無直接證實 meropenem 治療細菌性關節炎療效之對照試驗，故證據等級僅達 L3，不宜視為一線適應症擴充。

**若要推進需要：**
- 補齊 DG001（TFDA/當地仿單警語與禁忌症，Blocking）— 這是進入 S1 安全性初評的必要前提，目前完全缺乏資料
- 補齊 DG002（DrugBank 完整作用機轉資料）— 強化機轉關聯性論證的正式文件基礎
- 因香港目前未上市（0 張許可證），需評估上市申請或供應管道，才能進一步推進臨床應用
- 針對細菌性關節炎（尤其明確致病菌別、抗藥性型態）設計前瞻性療效研究或高品質回溯性對照研究，以提升證據等級至 L2 以上
- 建立目標病原菌藥敏監測機制（特別排除 MRSA 等 meropenem 無效菌株情境），避免不當經驗性使用
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

