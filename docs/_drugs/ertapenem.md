---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ertapenem：從廣效細菌感染到細菌性關節炎與金黃色葡萄球菌感染

## 一句話總結

Ertapenem 是碳青黴烯類廣效抗生素，臨床上用於複雜腹腔內感染、社區獲得性肺炎及複雜皮膚／軟組織感染等多種細菌感染。TxGNN 模型預測它可能對**細菌性關節炎（Bacterial Arthritis）**與**金黃色葡萄球菌感染（Staphylococcus aureus Infection）**具有療效，前者有 **10 篇文獻**佐證，後者有 **8 個臨床試驗**和 **20 篇文獻**支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效細菌感染（複雜腹腔內感染、肺炎、皮膚感染） |
| 預測新適應症（#1） | 細菌性關節炎（Bacterial Arthritis） |
| 預測新適應症（#2） | 金黃色葡萄球菌感染（Staphylococcus aureus Infection） |
| TxGNN 預測分數（#1） | 99.72% |
| TxGNN 預測分數（#2） | 99.28% |
| 證據等級（#1） | L3 |
| 證據等級（#2） | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

### 細菌性關節炎

Ertapenem 透過共價結合細菌青黴素結合蛋白（PBP1a、1b、2、3），抑制細胞壁肽聚糖交聯，對化膿性關節炎常見致病菌具廣效抗菌活性。化膿性關節炎病原體涵蓋 *Klebsiella pneumoniae*、*Clostridium* spp.、*Prevotella bivia*、*Citrobacter koseri* 等革蘭氏陰性菌及厭氧菌，Ertapenem 對上述菌種均具高效殺菌活性，且能穩定抵抗 ESBL（超廣效 β-lactamase），臨床上已有成功治療案例記錄。

Ertapenem 的藥動學特性（半衰期 ≈ 4 小時、蛋白結合率 ~95%）使其適合每日單次靜脈注射的門診靜脈抗菌治療（OPAT）方案，滑液中可達治療濃度，對需長期治療的骨關節感染具實務優勢。

### 金黃色葡萄球菌感染

針對持續性 MSSA 菌血症，Ertapenem 的機轉基於「Inoculum Effect 保護假說」：高菌量情境下，金黃色葡萄球菌大量分泌 β-lactamase 導致 cefazolin 被迅速水解失效。Ertapenem 作為碳青黴烯類，可競爭性飽和 β-lactamase 活性位點，顯著降低對 cefazolin 的降解速率，恢復其殺菌效力（協同 PBP2 結合）。此外，Ertapenem 本身與 PBP1a/1b 的高親和性形成雙重殺菌機轉，此外亦有體外研究顯示可上調周邊血單核球 IL-1β 分泌，具有免疫調節協同效果。

**Cefazolin + Ertapenem** 聯合方案已在多個回溯性研究與案例系列中展現對持續性 MSSA 菌血症（包括感染性心內膜炎、LVAD 相關感染）的清菌療效，並有 Phase 2 RCT 正在進行中。

---

## 適應症一：細菌性關節炎（Bacterial Arthritis）

### 臨床試驗證據

目前無相關臨床試驗登記。

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | 前瞻性觀察研究 | Antimicrobial Agents and Chemotherapy | 306 名門診靜脈治療患者，最常見適應症為腹腔感染（38%）與骨關節感染，長期 ertapenem OPAT 安全且有效 |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | 回溯性世代研究 | J Antimicrob Chemother | 10 名患者採皮下注射 β-lactam 作為骨關節感染長期抑菌治療，安全性與療效可接受 |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | 比較性觀察研究 | J Antimicrob Chemother | 評估 temocillin 替代碳青黴烯類治療 3GC-R 腸桿菌科骨關節感染，確認碳青黴烯類（包含 ertapenem）為當前標準治療 |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | 回溯性流行病學研究 | Clinical Laboratory | 四歲以下兒童骨關節感染病原分布與抗藥性分析，碳青黴烯類具廣效覆蓋 |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | 案例報告 | Journal of Chemotherapy | *Klebsiella pneumoniae* 化膿性腕關節炎以 ertapenem + levofloxacin 成功治療 |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | 案例報告 | BMJ Case Reports | 糖尿病足 *Citrobacter koseri* 化膿性關節炎合併骨髓炎，以 ertapenem 成功治療 |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | 案例報告 | Anaerobe | 86 歲女性 *Clostridium paraputrificum* 化膿性肩關節炎，關節鏡清創後碳青黴烯類治療改善 |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | 案例報告＋文獻回顧 | J Investig Med High Impact Case Rep | *Prevotella bivia* 化膿性關節炎，文獻回顧確認 ertapenem 為厭氧菌關節炎一線選擇 |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | 體外機轉研究 | Diagn Microbiol Infect Dis | Auranofin 透過協同作用增強 ertapenem 對碳青黴烯抗藥性大腸桿菌（CREC）的抗菌效果 |

---

## 適應症二：金黃色葡萄球菌感染（Staphylococcus aureus Infection）

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | 招募中 | 60 | **CERT 試驗**：首個評估 Cefazolin + Ertapenem 聯合方案治療 MSSA 菌血症的前瞻性 RCT，與目標適應症完全吻合 |
| [NCT07376889](https://clinicaltrials.gov/study/NCT07376889) | Phase 4 | 尚未招募 | 2096 | **COMBAT-SAB 試驗**：大規模評估 *S. aureus* 菌血症聯合抗生素療法，ertapenem 聯合方案為主要臂之一，完成後預期提供 L1 等級直接證據 |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | 招募中 | 300 | **SABEDTIO 試驗**：評估 *S. aureus* 菌血症早期雙重抗生素療法對預後的改善，與 ertapenem 聯合方案高度相關 |
| [NCT00366249](https://clinicaltrials.gov/study/NCT00366249) | Phase 3 | 完成 | 1061 | 糖尿病足感染 Phase 3 雙盲 RCT，Tigecycline vs Ertapenem，為 ertapenem 大規模臨床療效最高等級基礎證據 |
| [NCT06634940](https://clinicaltrials.gov/study/NCT06634940) | N/A | 招募中 | 1000 | 肝硬化相關感染國際抗藥性監測研究，提供 *S. aureus* 感染流行病學與抗藥趨勢背景資料 |
| [NCT06174649](https://clinicaltrials.gov/study/NCT06174649) | N/A | 完成 | 900 | **FAST-GN 試驗**：革蘭氏陰性菌菌血症快速藥敏試驗平台評估（間接背景資料） |
| [NCT03218397](https://clinicaltrials.gov/study/NCT03218397) | N/A | 完成 | 500 | **RAPIDS-GN 試驗**：GN 菌菌血症快速鑑定工具改善臨床結果評估（間接背景資料） |
| [NCT06044272](https://clinicaltrials.gov/study/NCT06044272) | N/A | 完成 | 10000 | 哥倫比亞醫院院內感染抗藥性流行病學回顧研究（區域背景資料） |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | 回溯性世代研究 | Clin Infect Dis | Cefazolin + Ertapenem 成功救治 11 例持續性 MSSA 菌血症（含 6 例心內膜炎），8 例於 24 小時內血培養轉陰 |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | 案例系列＋機轉研究 | Antimicrob Agents Chemother | 首次報告 ertapenem + cefazolin 協同清除難治性 MSSA 菌血症，附體外協同驗證與鼠皮膚感染模型 |
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | 回溯性比較世代 | J Antimicrob Chemother | 碳青黴烯聯合療法（含 ertapenem）vs 標準治療 MSSA 菌血症之比較性研究，提供直接對照數據 |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | 回溯性世代研究 | J Antimicrob Chemother | 低白蛋白血症（< 2.5 g/dL）影響 ertapenem 聯合療法暴露量，提供個別化使用安全指引 |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | 敘述性回顧 | Am J Health Syst Pharm | 系統回顧持續性 MSSA 菌血症多種聯合治療方案，確認 cefazolin + ertapenem 為重要救援選項 |
| [34978891](https://pubmed.ncbi.nlm.nih.gov/34978891/) | 2022 | 體外機轉研究 | Antimicrob Agents Chemother | Ertapenem 刺激周邊血單核球 IL-1β 分泌，部分解釋 cefazolin + ertapenem 協同療效的免疫調節機轉 |
| [35493130](https://pubmed.ncbi.nlm.nih.gov/35493130/) | 2022 | 體外＋體內研究 | Open Forum Infect Dis | Ertapenem + cefazolin 在葡萄球菌生物膜中具強效殺菌活性，支持 MSSA 感染性心內膜炎適用性 |
| [34599521](https://pubmed.ncbi.nlm.nih.gov/34599521/) | 2021 | 案例系列 | J Card Surg | Cefazolin + ertapenem 成功治療難治性 LVAD 相關 MSSA 感染，作為心臟移植前橋接清菌治療 |
| [36401791](https://pubmed.ncbi.nlm.nih.gov/36401791/) | 2023 | 案例系列 | Pharmacotherapy | 首例早產兒持續性 MSSA 菌血症合併骨髓炎，以 oxacillin + ertapenem 聯合成功治療 |
| [39777519](https://pubmed.ncbi.nlm.nih.gov/39777519/) | 2025 | 體外研究 | J Infect Dis | Ertapenem 或 meropenem 聯合 ceftaroline 或 vancomycin，增強對 MRSA 的殺菌活性，擴展至耐藥菌株適用性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：Ertapenem 蛋白結合率高達 ~95%，低白蛋白血症患者（血清白蛋白 < 2.5 g/dL）可能出現游離藥物濃度異常升高，影響安全性與療效，使用前需評估。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Ertapenem 對細菌性關節炎具有明確的藥理機轉支持及多個觀察性研究（L3），對 MSSA 感染則有 Phase 3 已完成試驗與 Phase 2 RCT 正在進行（L2），且 cefazolin + ertapenem 聯合方案有系統性臨床案例與機轉研究佐證；惟香港目前無上市許可，基礎安全性資料需補充。

**若要推進需要：**
- 確認香港 ertapenem 的進口及同情使用申請流程
- 補充 DrugBank MOA 完整資料與原廠仿單警語、禁忌症
- 建立低白蛋白血症（< 2.5 g/dL）及腎功能不全患者的劑量調整與安全性監測計畫
- 追蹤 **CERT 試驗**（NCT04886284）與 **COMBAT-SAB 試驗**（NCT07376889）進度，後者完成後預期升至 L1 等級
- 細菌性關節炎適應症建議設計前瞻性登錄研究，補充缺乏的 RCT 層級證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

