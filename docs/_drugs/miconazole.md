---
layout: default
title: Miconazole
parent: 中證據等級 (L3-L4)
nav_order: 583
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-14
description: "Miconazole：預測新適應症為痤瘡 (Acne)（證據等級 L3）。原適應症：足癬、體癬、皮膚念珠菌症、甲癬、花斑癬、外陰陰道念珠菌症等"
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
---

# Miconazole
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

## Miconazole：從皮膚黴菌感染與念珠菌症到痤瘡
{: .text-alpha }

## 一句話總結

Miconazole 是咪唑類（imidazole）抗黴菌藥，原本用於足癬、體癬、皮膚念珠菌症、外陰陰道念珠菌症等黴菌感染。
TxGNN 模型預測它可能對**痤瘡 (Acne)** 有效，
目前**沒有臨床試驗登記**，僅有 **4 篇文獻**（1 篇回顧、1 篇split-face臨床研究、1 篇治療試驗、1 篇體外研究）提供間接支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 足癬、體癬、皮膚念珠菌症、甲癬、花斑癬、外陰陰道念珠菌症等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（藥物資料庫中的 MOA 欄位為空）。根據已知的藥物類別資訊，Miconazole 屬於咪唑類抗黴菌藥，透過抑制 CYP51（羊毛固醇 14-α-去甲基酶）來阻斷黴菌麥角固醇合成。以下推論來自類別機轉，而非藥物專屬的整理資料。

Miconazole 與痤瘡的關聯，大致有三條可能路徑：

1. **抗菌作用**：體外研究顯示，唑類抗黴菌藥對痤瘡致病菌 *Cutibacterium (Propionibacterium) acnes* 有活性（PMID 20045949）。
2. **Malassezia 毛囊炎**：Malassezia（糠秕孢子菌）毛囊炎在臨床上常被誤診為痤瘡，抗黴菌藥對其有效（PMID 8593718）。這代表部分「痤瘡樣」病灶可能其實是黴菌所致，不等同於一般尋常痤瘡。
3. **抗發炎作用**：有文獻提到 Miconazole 在皮膚上具抗發炎效果，可能有助於發炎性病灶（PMID 18627330、15536660）。

TxGNN 分數很高（0.995），但這是計算預測，不能取代臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | 回顧 Miconazole 在多種皮膚疾患的作用，包含抗發炎等多面向效果 |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | 臨床研究（split-face） | Skin Res Technol | 以半臉對照與生物儀器評估輕度發炎性經期痤瘡的處理；規模可能偏小、非關鍵性試驗 |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | 臨床治療試驗 | Clin Exp Dermatol | 沙烏地阿拉伯 62 名 Pityrosporum 毛囊炎患者的診斷與治療；此病常被誤診為痤瘡，並非真正的尋常痤瘡 |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | 體外研究 | Biol Pharm Bull | 唑類抗黴菌藥對痤瘡患者分離的 *P. acnes* 具體外抗菌活性 |

## 香港上市資訊

Miconazole 在香港共有 20 張有效單一成分許可證，無已註銷者。下列為其中 5 張主要許可證（許可證資料中未載明劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45780 | DECOZOL CREAM 2% | 乳膏（依品名） | 未載明 |
| HK-68769 | MICODERM CREAM 2% W/W | 乳膏（依品名） | 未載明 |
| HK-45689 | AXCEL MICONAZOLE CREAM 2% | 乳膏（依品名） | 未載明 |
| HK-18530 | DAFRIN VAG TAB 100MG | 陰道錠（依品名） | 未載明 |
| HK-57834 | GYNO-MICOZO VAGINAL SOFT CAPSULE 0.4G | 陰道軟膠囊（依品名） | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝臟疾病、膽囊疾病（來自知識圖譜的藥物-疾病關聯，並非仿單原文，需以仿單核實）。
- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分範例：
  - 中度：Paclitaxel、Fentanyl、Acalabrutinib、Nifedipine、Ethinylestradiol、Alprazolam、Amiodarone、Amitriptyline、Amlodipine、Hydrocodone 等
  - 輕度：Dolutegravir、Loratadine、Amphotericin B、Ambrisentan 等

  這些資料多屬全身性使用時的考量；外用或陰道給藥的全身吸收較低，臨床意義需另行評估。

仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何痤瘡的臨床試驗，文獻僅有回顧、小型臨床研究及體外研究，其中一篇針對的是易與痤瘡混淆的 Malassezia 毛囊炎。高 TxGNN 分數僅代表計算預測。
- 仿單安全性資料與作用機轉資料仍有缺口，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署核准仿單，完成警語與禁忌症的解析
- 補齊 Miconazole 的作用機轉資料（例如查詢 DrugBank）
- 與現行痤瘡標準治療比較，評估外用 Miconazole 相對的價值
- 設計小型隨機對照試驗，區分尋常痤瘡與 Malassezia 毛囊炎的療效
- 確認適合痤瘡的外用劑型與濃度（香港現有製劑為 2% 乳膏及陰道製劑）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

