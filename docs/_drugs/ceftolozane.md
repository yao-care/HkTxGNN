---
layout: default
title: Ceftolozane
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Ceftolozane
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

# Ceftolozane：從複雜性尿路感染到淋球菌性尿道炎

## 一句話總結

Ceftolozane 是新型第五代頭孢菌素類抗生素，通常與 tazobactam 合併使用（商品名 Zerbaxa），已於美國及歐盟核准用於複雜性尿路感染及複雜性腹腔感染，但香港目前尚未上市。
TxGNN 模型預測它可能對**淋球菌性尿道炎 (Gonococcal Urethritis)** 有效，
然而目前有 **0 個臨床試驗**和 **0 篇文獻**直接支持此方向，證據完全來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 複雜性尿路感染、複雜性腹腔感染（美歐已核准；香港未上市，無本地許可）|
| 預測新適應症 | 淋球菌性尿道炎 (Gonococcal Urethritis) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ceftolozane 屬於 β-lactam 類抗生素（頭孢菌素），主要透過結合細菌的青黴素結合蛋白（PBP）來抑制細胞壁合成，對多種革蘭氏陰性菌具殺菌活性。

淋球菌（*Neisseria gonorrhoeae*）為革蘭氏陰性雙球菌，β-lactam 類藥物理論上具有機轉上的弱相關性——這也是 TxGNN 給出高預測分數的主要依據。然而，*N. gonorrhoeae* 對頭孢菌素的耐藥性正快速上升（產 ESBL 及質體媒介 β-lactamase），現行 CDC 及 WHO 淋病治療指引均以 ceftriaxone 為第一線，並不包含 Ceftolozane，且本藥在淋病領域亦無任何臨床試驗或文獻記錄。

綜合而言，機轉上雖有弱相關性，但因耐藥性屏障及完全缺乏臨床數據，本預測的臨床轉化可行性極低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Ceftolozane 在香港目前**未取得衛生署藥物許可**，無任何本地上市紀錄。

Ceftolozane/Tazobactam（Zerbaxa）已於以下地區取得核准，可供未來引進參考：

| 地區 | 核准機構 | 核准年份 | 主要核准適應症 |
|------|---------|---------|--------------|
| 美國 | FDA | 2014 | 複雜性尿路感染（含腎盂腎炎）、複雜性腹腔感染（合併 metronidazole）|
| 歐盟 | EMA | 2015 | 複雜性尿路感染、複雜性腹腔感染 |
| 美國（擴充） | FDA | 2019 | 醫院獲得性肺炎／呼吸器相關肺炎（HABP/VABP） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Ceftolozane 在香港尚未上市，最高排名預測適應症（淋球菌性尿道炎）缺乏任何臨床試驗或文獻支持（L5），且目標病原體的耐藥性使機轉上的弱關聯難以轉化為臨床效益；其餘預測適應症中，多項（Ureaplasma 尿道炎、泌尿生殖道結核、先天性無白蛋白血症、血型不相容、前惡性血液病等）與抗生素機轉完全不相符，屬知識圖譜路徑雜訊，排除使用。

**若要推進需要：**
- 取得原廠 FDA/EMA 仿單，確認完整安全性警語與禁忌症
- 調查 Ceftolozane 對當前流行 *N. gonorrhoeae* 菌株的體外抗菌活性（MIC 數據）
- 確認現行難治性淋病是否存在未被滿足的用藥需求缺口（尤其多重耐藥菌株）
- 補充 DrugBank MOA 資料，強化機轉關聯性分析
- 若認為黃色肉芽腫性腎盂腎炎（Rank 4，L4，Research Question）有研究價值，可優先評估此適應症，因 Ceftolozane/tazobactam 已有腎盂腎炎核准適應症，機轉延伸更為合理
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

