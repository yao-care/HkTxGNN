---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 778
evidence_level: L5
indication_count: 5
---

# Ruxolitinib
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

# Ruxolitinib：從原適應症未登載到子宮血管周上皮樣細胞瘤

## 一句話總結

Ruxolitinib 是 JAK1/JAK2 抑制劑，在香港已有 5 張許可證（Jakavi 口服錠及 Lumirix 乳膏），但資料中未載明原適應症。
TxGNN 模型預測它可能對**子宮體血管周上皮樣細胞瘤 (uterine corpus perivascular epithelioid cell tumor)** 有效。
目前**沒有臨床試驗與文獻**直接支持此預測，僅有模型分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供 |
| 預測新適應症 | 子宮體血管周上皮樣細胞瘤 (uterine corpus perivascular epithelioid cell tumor) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ruxolitinib 是 JAK1/JAK2 抑制劑，作用於 JAK-STAT 訊號路徑。

血管周上皮樣細胞瘤（PEComa）通常由 TSC1/TSC2 功能喪失和 mTOR 過度活化所驅動。目前提供的資料中，並沒有支持 JAK-STAT 訊號與 PEComa 生物學之間存在直接關聯的證據。若透過 mTOR 與 JAK-STAT 的交互作用來解釋，目前仍屬推測。

TxGNN 的高分（0.997）較可能反映知識圖譜中相關疾病節點的鄰近性，而非獨立的實證證據。

### 其他預測適應症（供參考）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 2 | 良性 PEComa (benign PEComa) | 99.73% | L5 | Hold |
| 3 | 淋巴管肌瘤 (lymphangiomyoma) | 99.72% | L5 | Hold |
| 4 | 淋巴管平滑肌瘤病 (lymphangioleiomyomatosis) | 99.64% | L5 | Hold |
| 5 | 脂肪肉瘤 (liposarcoma) | 99.52% | L4 | Research Question |

排名 2–4 同屬 TSC/mTOR 軸相關疾病，同樣缺乏 JAK 抑制的直接證據。排名 5 的脂肪肉瘤有間接的前臨床證據：兩篇研究顯示，黏液樣脂肪肉瘤中 FUS-DDIT3 融合致癌蛋白會影響 JAK-STAT 訊號，且該訊號控制癌幹細胞特性與化療抗藥性。這為 JAK 抑制提供了合理的假說，但僅限於前臨床模型與黏液樣亞型，尚無患者的療效或安全性資料。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

針對首位預測適應症（子宮體 PEComa），目前無相關文獻。

脂肪肉瘤（排名 5）的間接文獻如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35186752](https://pubmed.ncbi.nlm.nih.gov/35186752/) | 2022 | 前臨床（細胞/機轉） | Frontiers in Oncology | FUS-DDIT3 融合蛋白表現會提高 STAT3 及磷酸化 STAT3 的水平，影響黏液樣脂肪肉瘤的 JAK-STAT 訊號 |
| [30650179](https://pubmed.ncbi.nlm.nih.gov/30650179/) | 2019 | 前臨床（細胞/機轉） | International Journal of Cancer | JAK-STAT 訊號控制黏液樣脂肪肉瘤的癌幹細胞特性，包括對 doxorubicin 的化療抗藥性 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61973 | JAKAVI TAB 5MG | 資料未提供 | 資料未提供 |
| HK-61972 | JAKAVI TAB 20MG | 資料未提供 | 資料未提供 |
| HK-61974 | JAKAVI TAB 15MG | 資料未提供 | 資料未提供 |
| HK-66148 | JAKAVI TABLETS 10MG | 資料未提供 | 資料未提供 |
| HK-68437 | LUMIRIX CREAM 15MG/G | 資料未提供 | 資料未提供 |

Jakavi 由 Novartis Pharmaceuticals (HK) Limited 持有，Lumirix 乳膏由 Rxilient Medical (Hong Kong) Limited 持有。

---

## 細胞毒性

Ruxolitinib 為標靶藥物（JAK 抑制劑），非傳統細胞毒性化療藥物，且資料中缺乏抗腫瘤分類與毒性資訊。請參考原廠仿單的警語與注意事項。

---

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢未找到資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有 PEComa 與 LAM 相關預測均只有模型分數，沒有試驗或文獻支持；而這些疾病由 TSC/mTOR 驅動，與 JAK1/2 抑制之間缺乏已證實的機轉連結。
- 脂肪肉瘤（排名 5）有間接前臨床證據，可作為研究問題（Research Question）進一步探索，但目前不足以支持臨床推進。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料（目前為阻斷性資料缺口，無法進入安全性篩選）
- 從 DrugBank 取得 MOA 資料，並補足原適應症資訊
- 建立 JAK-STAT 與 mTOR 路徑在 PEComa/LAM 的機轉證據（細胞或動物模型）
- 針對黏液樣脂肪肉瘤，檢視 ruxolitinib 的前臨床療效資料，並搜尋相關臨床試驗

---

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

