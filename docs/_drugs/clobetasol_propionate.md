---
layout: default
title: Clobetasol Propionate
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 7
---

# Clobetasol Propionate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Clobetasol Propionate：從外用強效皮質類固醇到外陰倒置性毛囊角化症

## 一句話總結

Clobetasol Propionate（丙酸氯倍他索）是外用強效糖皮質激素，香港許可證資料未載明原適應症。
TxGNN 模型預測它可能對**外陰倒置性毛囊角化症 (Vulvar Inverted Follicular Keratosis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 外陰倒置性毛囊角化症 (Vulvar Inverted Follicular Keratosis) |
| TxGNN 預測分數 | 99.46% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Clobetasol 是外用強效糖皮質激素受體促效劑，
機轉上可產生抗發炎作用，因此在發炎性皮膚疾病中有理論上的用途。

不過，倒置性毛囊角化症一般被視為良性、非發炎性的病灶。
抗發炎作用與這個疾病的病理之間關聯薄弱。
目前唯一的支持只有 TxGNN 的高分（0.995），沒有其他機轉或臨床佐證，因此這個預測的合理性偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-36493 | SENSODERM CREAM | MEYER PHARMACEUTICALS LTD |
| HK-55796 | CLOBETASOL PROPIONATE | UNICO & CO |
| HK-64930 | POWERCORT CREAM 0.05% W/W | UP SUPREME (HK) LIMITED |
| HK-43905 | UNIDERM CREAM 0.05% | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-37528 | SENSODERM OINTMENT | MEYER PHARMACEUTICALS LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有試驗、文獻，機轉上也缺乏合理性（病灶屬非發炎性）。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料
- 補齊 DrugBank 的作用機轉資料
- 針對倒置性毛囊角化症做專門的文獻檢索，確認是否有類固醇治療的病例或研究
- 確認此疾病是否有外用治療的臨床需求

**其他候選適應症（供參考）：** 同一批預測中，證據較充分的是以下兩項，可考慮優先評估。
- **Exanthem（皮疹）**（排名 3，L3）：有多項 clobetasol 相關試驗，但多為口腔扁平苔癬、外陰硬化性苔癬等相近的發炎性疾病，並非直接針對皮疹。
- **瘢痕疙瘩性痤瘡 (Acne Keloidalis)**（排名 4，L4）：有一項 20 人的開放標籤研究，比較 clobetasol 與 betamethasone 泡沫劑。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

