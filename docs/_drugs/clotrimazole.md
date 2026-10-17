---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Clotrimazole：預測新適應症為痤瘡 (Acne)（證據等級 L5）。原適應症：足癬、體癬、皮膚念珠菌症、花斑癬、口腔念珠菌症、外陰陰道念珠菌症等"
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
---

# Clotrimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clotrimazole：從皮膚與黏膜黴菌感染到外陰陰道炎

## 一句話總結

Clotrimazole 是一種唑類（azole）抗黴菌藥，原本用於足癬、體癬、皮膚念珠菌症、口腔念珠菌症及外陰陰道念珠菌症等黴菌感染。
TxGNN 模型預測排名第一的新適應症為**痤瘡 (acne)**，但目前僅有 **1 個複方試驗**，且無文獻支持，證據薄弱。
預測排名第二的**外陰陰道炎 (vulvovaginitis)** 有 **12 個臨床試驗**和 **20 篇文獻**，但這其實是既有核准用途的延伸，並非真正的新適應症。

> 本報告依預測排名，以排名第一的痤瘡為主要評估對象，並在後續章節補充說明外陰陰道炎與萎縮性陰道炎。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 足癬、體癬、皮膚念珠菌症、花斑癬、口腔念珠菌症、外陰陰道念珠菌症等（取自知識圖譜；許可證資料未載明核准適應症文字） |
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4（痤瘡）；外陰陰道炎為 L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（痤瘡）；外陰陰道炎為 Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，clotrimazole 是唑類抗黴菌藥，一般認為它抑制黴菌 CYP51（羊毛固醇 14-α-去甲基酶），干擾麥角固醇合成並破壞黴菌細胞膜完整性。此外也有報告指出它具一定的抗菌與抗發炎活性。

就痤瘡而言，可能的關聯在於 Malassezia 或 Cutibacterium 相關的毛囊發炎，但這一點屬於推測。唯一找到的試驗是含 beclomethasone、gentamicin 與 clotrimazole 的固定複方，無法歸因於 clotrimazole 單一成分。TxGNN 的高分是運算預測，不能取代臨床證據。

排名第二的外陰陰道炎（特別是念珠菌性）本來就是 clotrimazole 的核心適應症，臨床證據充足，屬於既有用途的確認。排名第三的停經後萎縮性陰道炎主要由雌激素缺乏引起，與黴菌感染無關，高分可能只是反映與其他陰道炎疾病在網路上的相近性，沒有明確的機轉依據。

---

## 臨床試驗證據

### 痤瘡（排名 1）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | 暫停 | 80 | beclomethasone + gentamicin + clotrimazole 複方乳膏用於污染性皮膚病變的比較療效；無完成結果，無法分離 clotrimazole 的貢獻 |

### 外陰陰道炎（排名 2，列出最相關的 10 個）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | 完成 | 466 | clotrimazole 500 mg 陰道栓劑對比陰道錠，非劣性研究 |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | 完成 | 1524 | 西非婦女陰道分泌物處置：單劑 tinidazole + fluconazole 對比 metronidazole + clotrimazole 較長療程 |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | 招募中 | 264 | clotrimazole + lactulose 複方對比 clotrimazole 單方（Canesten®），尚無結果 |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | 完成 | 150 | dequalinium chloride 10 mg 對比 clotrimazole 100 mg 治療外陰陰道念珠菌症 |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | 完成 | 240 | clotrimazole 陰道錠對比 fluconazole 治療重度外陰陰道念珠菌症 |
| [NCT03115073](https://clinicaltrials.gov/study/NCT03115073) | Phase 2/3 | 完成 | 84 | ProF-001 (Candiplus®) 劑量遞增，以 1% clotrimazole 陰道乳膏為對照 |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | 完成 | 100 | 孜然籽萃取物陰道栓劑，clotrimazole 可能為對照 |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | 完成 | 140 | clotrimazole 陰道錠加口服乳酸桿菌，預防復發性念珠菌症 |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | N/A | 完成 | 1033 | Empecid L 乳膏 (clotrimazole 1%) 上市後安全性問卷調查 |
| [NCT03024502](https://clinicaltrials.gov/study/NCT03024502) | Phase 1/2 | 未知 | 90 | 含 propolis 萃取物之黏膜貼附凝膠，與 clotrimazole 乳膏比較 |

> 另有 NCT02248506、NCT04292704、NCT02907307（已撤銷，0 人）等試驗，因相關性較低或未執行，未列入。

### 停經後萎縮性陰道炎（排名 3）

目前無相關臨床試驗登記。

---

## 文獻證據

痤瘡目前無相關文獻。以下為外陰陰道炎相關文獻（優先列 RCT，其次為回顧與其他研究）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | 199 名患者，比較單劑 500 mg 與 6 日 100 mg clotrimazole 陰道錠治療念珠菌性外陰陰道炎的療效與耐受性 |
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complement Ther Med | Prangos ferulacea 陰道乳膏對比 clotrimazole 陰道乳膏 |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | 益生菌與乳鐵蛋白作為復發性外陰陰道念珠菌症的維持治療 |
| [40855225](https://pubmed.ncbi.nlm.nih.gov/40855225/) | 2025 | RCT | AAPS PharmSciTech | voriconazole 載體 spanlastics 治療外陰陰道念珠菌症 |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | 雙盲隨機研究 | Obstet Gynecol | 42 名復發性念珠菌陰道炎患者，clotrimazole 500 mg 栓劑每週一次共兩週，90.4% 臨床緩解 |
| [32992877](https://pubmed.ncbi.nlm.nih.gov/32992877/) | 2020 | 系統性回顧 | Pharmaceuticals (Basel) | clotrimazole 治療外陰陰道念珠菌症逾 45 年的臨床經驗彙整 |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | J Appl Microbiol | clotrimazole 作為藥物的過去、現在與未來 |
| [39432168](https://pubmed.ncbi.nlm.nih.gov/39432168/) | 2024 | 回溯性分析 | Mycopathologia | 1303 例重度外陰陰道念珠菌症，比較 clotrimazole 與 fluconazole 不同療程，三劑療法效果較佳 |
| [41350226](https://pubmed.ncbi.nlm.nih.gov/41350226/) | 2025 | Cohort | Pharmacoepidemiol Drug Saf | 日本大型資料庫研究，孕早期外用抗黴菌藥與重大先天畸形風險 |
| [40886781](https://pubmed.ncbi.nlm.nih.gov/40886781/) | 2025 | 體外/離體機轉研究 | Pharmacol Res | 經典唑類抗黴菌藥（含 clotrimazole）影響人類足月胎盤模型的類固醇生成活性 |

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑，無已註銷者。下表列出 5 張主要許可證（資料中未載明劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-25433 | CANESTEN CREAM 1%（Bayer） | 乳膏（依品名） | 未載明 |
| HK-25432 | CANESTEN VAGINAL TAB 0.1G（Bayer） | 陰道錠（依品名） | 未載明 |
| HK-65884 | CANESTEN ANTI FUNGAL CREAM 1% W/W（Bayer） | 乳膏（依品名） | 未載明 |
| HK-47412 | GEOVITE SKIN SPRAY 1%（Meyer） | 皮膚噴劑（依品名） | 未載明 |
| HK-65810 | CLOTRI CUTANEOUS SPRAY, SOLUTION 10MG/ML（Hitpharm） | 皮膚噴劑（依品名） | 未載明 |

---

## 安全性考量

- **知識圖譜標示之相關疾病（非仿單內容）**：腎上腺皮質功能不全、艾迪生氏病、皮膚萎縮、微血管擴張、微血管疾病、遺傳性出血性微血管擴張症、周邊血管疾病、間歇性跛行、周邊動脈疾病。
- **藥物交互作用**：資料庫共查得 100 筆，其中較重要的有：
  - **Major（嚴重）**：Fentanyl、Alfentanil、Amiodarone、Hydrocodone
  - **Moderate（中度）**：Abemaciclib、Paclitaxel、Acalabrutinib、Nifedipine、Levonorgestrel、Estradiol、Alprazolam、Apixaban、Aprepitant 等
  - **Minor（輕微）**：Dolutegravir、Amphotericin B
- **妊娠相關**：有研究探討孕早期外用抗黴菌藥與先天畸形風險，以及唑類藥物對胎盤類固醇生成的影響，孕婦使用時需留意。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：**
- **痤瘡：Hold**
- **外陰陰道炎（念珠菌性）：Proceed with Guardrails**
- **停經後萎縮性陰道炎：Hold**

**理由：**
- 痤瘡僅有一個暫停中的三合一複方試驗，無法歸因於 clotrimazole，機轉關聯也屬推測，TxGNN 高分不足以支持推進。
- 外陰陰道炎已有多個已完成的 Phase 3 試驗與長期臨床經驗，證據等級 L1，但這是既有核准用途的確認，不是新的再利用機會。
- 萎縮性陰道炎的病因為雌激素缺乏，與 clotrimazole 的機轉無明確關聯，且完全沒有試驗或文獻。

**若要推進需要：**
- 痤瘡：clotrimazole 單一成分的對照試驗，並釐清與 Malassezia 或 Cutibacterium 毛囊發炎的關聯。
- 外陰陰道炎：證據僅適用於念珠菌性，不應外推至細菌性陰道病或滴蟲症；孕早期暴露與胎盤類固醇生成影響需持續關注。
- 補齊香港仿單的警語、禁忌症與核准適應症文字（目前缺漏，安全性篩查尚無法完成），並取得詳細的作用機轉資料。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

