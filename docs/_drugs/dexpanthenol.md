---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "DEXPANTHENOL"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "exanthem (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Dexpanthenol：預測新適應症為肛門直腸狹窄 (anorectal stricture)（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Dexpanthenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Dexpanthenol: 肛門直腸狹窄 (anorectal stricture)
{: .text-alpha }

## 一句話總結

Dexpanthenol 是泛酸（維生素 B5）的前驅物，原本用於皮膚疾病（如皮膚炎、濕疹）及腸胃動力障礙（如麻痺性腸阻塞、胃輕癱）。
TxGNN 模型預測分數最高的新適應症是**肛門直腸狹窄 (Anorectal Stricture)**，但目前**沒有臨床試驗與文獻**支持，僅為模型預測。
若看有實際試驗的預測方向，則是**發疹 (Exanthem)**，有 **1 個 Phase 3 試驗**（間接證據）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肛門直腸狹窄 (anorectal stricture) |
| TxGNN 預測分數 | 0.9972 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

> 其他預測適應症（依 TxGNN 分數排序）：無肛 (Imperforate Anus, 0.9971)、肛門息肉 (Anal Polyp, 0.9962)、外陰倒置性毛囊角化症 (0.9960)、直腸炎 (Proctitis, 0.9960)、發疹 (Exanthem, 0.9960)、點狀上皮角膜結膜炎 (0.9934)。其中僅「發疹」有相關臨床試驗。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dexpanthenol 是泛酸（輔酶 A 的前驅物）的前驅藥，被認為能促進上皮傷口癒合與組織修復。

肛門直腸狹窄常與黏膜損傷後的癒合與纖維化有關，因此「促進黏膜癒合」在理論上有些關聯。此外，原適應症包含腸胃動力障礙，與下消化道疾病有間接連結。但這種關聯相當鬆散，屬於推測，並無實證。

其他預測方向的合理性不一：直腸炎（黏膜癒合與抗發炎）和點狀上皮角膜結膜炎（角膜上皮修復）有可想像的機轉；無關聯較弱者如肛門息肉（結構性病灶，通常以切除處理）、無肛（先天畸形，需手術矯正）；外陰倒置性毛囊角化症的分數來自 TxGNN 模型（深度學習），可能只是反映模型學到的相關疾病之間的相似性，而非生物學證據，Dexpanthenol 的保濕與皮膚屏障作用並不知可治療角化病灶。

---

## 臨床試驗證據

首要預測適應症（肛門直腸狹窄）目前無相關臨床試驗登記。

以下為排名第 6 的「發疹」預測所對應的試驗（間接證據）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | 完成 | 160 | 隨機雙盲，比較 Bepanthen® 乳膏（含 Dexpanthenol）與 Cetomacrogol 乳膏，預防接受 EGFR 抑制劑患者的丘疹膿皰性皮疹；未提供結果，療效無法判斷 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-55710 | CORNEREGEL EYE GEL 50MG/G | 單一成分 | BAUSCH & LOMB (HK) LTD | 有效 |
| HK-43879 | SICCAPROTECT EYE DROPS | 複方 | REICH PHARM LIMITED | 有效 |

<!-- licenses:end -->

上表許可證包括單一成分與複方製劑（SICCAPROTECT EYE DROPS 另含 polyvinyl alcohol），皆為眼科製劑；狀態見表中「狀態」欄。

<!-- review:begin hk-lic-20261124b-dexpanthenol-1 -->

> **查核更正（2026-11-24）**：原文為「兩張許可證均為單方、有效狀態，皆為眼科製劑。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-dexpanthenol-1 -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：血友病 (hemophilia)（來自知識圖譜，非仿單內容）
- **藥物交互作用**：查詢無資料

其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（肛門直腸狹窄）及多數其他預測僅有模型分數，無任何臨床試驗或文獻，證據等級為 L5。
- 唯一相關的 Phase 3 試驗針對的是 EGFR 抑制劑引起的皮疹預防，與預測的「發疹」只有間接關聯，且結果未提供。此外，香港現有許可證均為眼科製劑，與腸道／肛門直腸給藥途徑不相符。

**若要推進需要：**
- 補充作用機轉（MOA）資料
- 取得香港衛生署仿單的警語與禁忌資訊
- 針對肛門直腸狹窄或直腸炎進行文獻與試驗檢索，並確認是否有合適的局部劑型（如肛門直腸用製劑）
- 取得 NCT01136005 的結果，評估其對皮膚反應的療效
- 若有意探索，優先考慮直腸炎、點狀上皮角膜結膜炎等機轉較合理的方向，並先做小規模概念驗證研究

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「兩張許可證均為單方、有效狀態，皆為眼科製劑。」→「上表許可證包括單一成分與複方製劑（SICCAPROTECT 」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

