---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acyclovir：預測新適應症為點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)（證據等級 L5）。原適應症：單純皰疹、帶狀皰疹、水痘、唇皰疹、單純皰疹腦炎、生殖器皰疹"
monitor_inn: "acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Acyclovir：從皰疹感染到點狀上皮角膜結膜炎

## 一句話總結

Acyclovir（阿昔洛韋）是抗皰疹病毒藥物，原本用於單純皰疹、帶狀皰疹、水痘、唇皰疹、單純皰疹腦炎及生殖器皰疹。
TxGNN 模型預測分數最高的新適應症是**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)**，但目前**沒有臨床試驗**，只有 **2 篇不直接相關的文獻**，證據僅屬模型預測層級。
在所有預測中，證據相對較多的是**尋常疣 (Common Wart)**：有 **4 個臨床試驗**和 **多篇文獻**，其中包含 1 個 Phase 2/3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 單純皰疹、帶狀皰疹、水痘、唇皰疹、單純皰疹腦炎、生殖器皰疹（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.67% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

**其他預測適應症概覽：**

| 排名 | 預測適應症 | 預測分數 | 證據等級 | 建議 |
|------|-----------|---------|---------|------|
| 2 | 尋常疣 (Common Wart) | 99.46% | L2 | 值得進一步研究 |
| 3 | 感染後神經痛 | 99.25% | L5 | Hold |
| 4 | C 型肝炎引起的肝硬化 | 99.23% | L5 | Hold |
| 5 | 嗜酸性膿皰性毛囊炎 | 99.22% | L5 | Hold |
| 6 | COVID-19 後遺症 | 99.16% | L4 | Hold |
| 7 | 外陰陰道念珠菌症 | 99.11% | L5 | Hold |
| 8 | 丘疹性蕁麻疹 | 99.09% | L5 | Hold |
| 9 | 眼眶區域疾病 | 99.08% | L2 | 值得進一步研究（多屬既有適應症延伸） |
| 10 | 流行性角結膜炎 | 99.07% | L4 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知藥理而言，acyclovir 經病毒胸苷激酶 (thymidine kinase) 活化後，抑制皰疹病毒 DNA 聚合酶。點狀上皮角膜炎可由 HSV 或 VZV 引起，因此在抗病毒層面有合理的連結。

然而，檢索到的兩篇文獻分別談**微孢子蟲角膜結膜炎**與**愛滋病患者的角膜脂質沉積症**，都不是 acyclovir 有效的疾病，沒有支持此預測的臨床證據。

在所有預測中，**尋常疣**的證據較具體。疣由 HPV 引起，HPV 沒有病毒胸苷激酶，所以標準的 acyclovir 活化途徑並不適用。病灶內注射的可能機轉包括非特異性抑制病毒 DNA 合成與免疫調節。多項小型隨機試驗（含 Phase 2/3 RCT 對照冷凍療法）正在比較病灶內 acyclovir 與其他療法，但樣本小、多為單中心，且多數狀態未知。

---

## 臨床試驗證據

**點狀上皮角膜結膜炎（排名 1）：** 目前無相關臨床試驗登記。

**尋常疣（排名 2，證據最完整的預測）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | 未知 | 92 | 足底疣：病灶內 acyclovir vs 冷凍療法的隨機對照試驗（已有對應發表 PMID 40889709） |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | 未知 | 40 | 足底疣：病灶內 acyclovir vs 念珠菌抗原 |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | 招募中 | 40 | 皮膚病毒疣：病灶內維生素 D3 vs acyclovir，尚無結果 |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | 不適用 | 未知 | 44 | 足底疣：病灶內維生素 D3 vs acyclovir |

**眼眶區域疾病（排名 9，與眼部皰疹相關的試驗）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06757907](https://clinicaltrials.gov/study/NCT06757907) | 不適用 | 完成 | 20 | 局部 ganciclovir vs 全身性 acyclovir 治療皰疹性角膜炎 |
| [NCT03389191](https://clinicaltrials.gov/study/NCT03389191) | 不適用 | 未知 | 30 | 口服 acyclovir 用於病毒性葡萄膜炎 |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | 不適用 | 未知 | 40 | 樹枝狀病毒性潰瘍的不同治療方式比較（非 acyclovir 專屬） |
| [NCT00031447](https://clinicaltrials.gov/study/NCT00031447) | Phase 3 | 完成 | 29 | 新生兒皮膚、眼、口 HSV 感染後口服 acyclovir 抑制療法（安慰劑對照）；與眼眶疾病的相關性不確定 |
| [NCT00000693](https://clinicaltrials.gov/study/NCT00000693) | 不適用 | 完成 | 25 | 高劑量靜脈 acyclovir 加 zidovudine 抑制愛滋病患者 CMV 視網膜炎（年代久遠、標的病原不同） |

另有 NCT03178149（ASP7317 用於地圖狀萎縮）與 acyclovir 無關，疑為誤配，不列入評估。

---

## 文獻證據

**尋常疣（排名 2）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | 病灶內 acyclovir vs 冷凍療法治療足底疣 |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | 病灶內 acyclovir vs B 型肝炎疫苗治療頑固性足底疣（48 人完成） |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | 系統性回顧／網絡統合分析 | Medicine | 比較各種皮膚疣治療方式，將病灶內 acyclovir 視為新興療法 |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | 比較研究 | Arch Dermatol Res | 病灶內 acyclovir vs 5-FU 治療頑固性疣 |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | 比較研究 | Arch Dermatol Res | 病灶內 acyclovir vs 四價 HPV 疫苗（60 人） |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | 比較研究 | Cureus | 病灶內 acyclovir vs PPD 免疫治療病毒疣 |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | 臨床研究 | J Cutan Med Surg | 病灶內 acyclovir 作為皮膚疣的潛在治療選項 |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | 病例＋文獻回顧 | Viruses | acyclovir／valacyclovir 使 HPV 相關疾病緩解的個案 |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | 臨床研究（個案） | J Drugs Dermatol | 口服 acyclovir 十天後頑固性足底疣消退 |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | 其他 | Cutis | acyclovir 軟膏用於尋常疣 |

另有數篇性傳染病、孕期皮膚感染等一般性回顧文獻，與本適應症僅間接相關，未列入。

**點狀上皮角膜結膜炎（排名 1）：** 僅有兩篇不直接相關的病例系列（[21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/)，微孢子蟲角膜結膜炎，2011；[7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/)，愛滋病患者角膜脂質沉積症，1995），無法支持此預測。

---

## 香港上市資訊

香港共有 20 張有效單一成分許可證，皆為上市狀態，無已註銷者。以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 製造商 |
|---------|------|-------|
| HK-30325 | ZOVIRAX TAB 400MG | GLAXOSMITHKLINE LIMITED |
| HK-25758 | ZOVIRAX SUSP ORAL 200MG/5ML | GLAXOSMITHKLINE LIMITED |
| HK-54026 | HERAX 400 TAB 400MG | HANG LUNG TRADING (H.K.) CO |
| HK-41261 | ACYCLOVIR 800 STADA TAB | HONG KONG MEDICAL SUPPLIES LTD |
| HK-58833 | GYNOVIR CREAM 5% | GAILY PHARMACEUTICAL COMPANY LIMITED |

此外另有多個 5% 乳膏與 200／400／800 mg 錠劑的學名藥許可證。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容，僅供參考）：** 高血壓、腎臟疾病與腎功能不全、高血糖與糖尿病（含酮酸中毒）、腎上腺皮質功能不全（Addison 病）、肥胖、中風與腦血管疾病、心肌梗塞、溶血性尿毒症候群、血栓性血小板減少性紫斑、周邊血管疾病、血紅素病變、皮膚萎縮與微血管擴張症等。
- **藥物交互作用：** 共 454 筆，以下為部分範例。
  - 中度：balsalazide、mesalazine、olsalazine、sulfasalazine、trospium
  - 等級未知：epinephrine、amphotericin B、mannitol、calcitriol、pantoprazole、glimepiride、doxycycline、metformin、omeprazole、morphine 等

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（針對排名第一的點狀上皮角膜結膜炎）

**理由：**
- 此預測僅有模型分數，無臨床試驗，檢索到的文獻與 acyclovir 無關，屬 L5。
- 排名 2 的**尋常疣**證據較佳（L2，含 Phase 2/3 RCT 與多項小型比較研究），可列為值得進一步研究的方向，但試驗樣本小、多為單中心、狀態多未知，且 HPV 缺乏胸苷激酶，機轉尚未釐清。
- 排名 9 的眼部皰疹相關疾病，大部分屬於既有適應症的延伸，並非真正的新用途。
- 其餘預測（C 型肝炎肝硬化、念珠菌症、流行性角結膜炎等）機轉上缺乏合理性，不建議推進。

**若要推進需要：**
- 優先針對尋常疣，等待或取得 NCT06261684 與 PMID 40889709 的完整結果，並進行多中心、較大樣本的 RCT 驗證
- 釐清病灶內 acyclovir 對 HPV 的作用機轉
- 補齊香港許可證的核准適應症與劑型，並確認病灶內注射不屬於現有核准給藥途徑，需評估藥事與法規可行性
- 取得作用機轉資料與仿單警語、禁忌，完成安全性評估
- 若仍要評估點狀上皮角膜結膜炎，需先確認病因是否為 HSV／VZV，再設計相應的臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

