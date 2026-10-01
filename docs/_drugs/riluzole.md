---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 759
evidence_level: L5
indication_count: 5
---

# Riluzole
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

# Riluzole：從原核准適應症（資料未載明）到雙側旁矢狀頂枕葉多小腦回畸形

## 一句話總結

Riluzole（利魯唑）已在香港上市，但本次資料中沒有記載它的原適應症。
TxGNN 模型預測它可能對**雙側旁矢狀頂枕葉多小腦回畸形 (Bilateral Parasagittal Parieto-occipital Polymicrogyria)** 有效。
目前**沒有臨床試驗和文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 雙側旁矢狀頂枕葉多小腦回畸形 (Bilateral Parasagittal Parieto-occipital Polymicrogyria) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。
根據預測的推論說明，Riluzole 是麩胺酸釋放抑制劑，也會調節鈉離子通道。

多小腦回畸形是胚胎發育期形成的大腦皮質結構異常。調節麩胺酸神經傳導，預期無法逆轉已形成的結構缺陷，因此**目前找不到明確的機轉連結**。

TxGNN 的高分更可能來自知識圖譜的拓撲關係，而不是已證實的生物學關聯。在現有資料中，這個預測沒有任何臨床或文獻證據佐證，應視為純模型預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-42525 | RILUTEK TAB 50MG | SANOFI HONG KONG LIMITED |
| HK-67243 | TEGLUTIK ORAL SUSPENSION 5MG/ML | LEE'S PHARMACEUTICAL (H.K) LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有任何臨床試驗或文獻佐證，機轉上也看不出合理的連結。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌症、核准適應症），這是目前的阻擋項。
- 補齊 Riluzole 的作用機轉（MOA）和原適應症資料，可從 DrugBank 取得。
- 做針對性的文獻搜尋，確認是否有多小腦回畸形相關的研究。
- 優先評估其他預測候選，其中以「晚發性成人下運動神經元症候群 (Lower Motor Neuron Syndrome with Late-adult Onset)」的生物學合理性最高。該疾病涉及運動神經元退化，與 Riluzole 的麩胺酸調節與神經保護機轉相符，但同樣沒有試驗或文獻佐證，下一步應針對 Riluzole 與下運動神經元疾病做文獻檢索。
- 其餘三個候選的機轉連結薄弱或缺乏支持，同樣維持 Hold：
  - 軸向脊椎干骺端發育不良 (Axial Spondylometaphyseal Dysplasia)：骨骼發育異常，與 Riluzole 的作用無已知關聯。
  - 多毛症-視網膜色素變性-侏儒症候群 (Trichomegaly-Retina Pigmentary Degeneration-Dwarfism Syndrome)：僅有推測性的視網膜神經保護理由。
  - 致死性關節攣縮-前角細胞疾病症候群 (Lethal Arthrogryposis-Anterior Horn Cell Disease Syndrome)：雖與運動神經元有鬆散關聯，但此病為先天性且致死，安全性與可行性存疑。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

